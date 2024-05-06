"""Module main"""
import time
import pickle
from datetime import datetime
import schedule
import redis

from api_requests.share_request import ShareInfo

SURVEY_PERIOD = 30

redis_client = redis.Redis(host='redis', port='6379')


def data_conversion():
    """ Создает экземпляр класса, сохраняет дату,
    время события и список пар,
    сериализует полученные данные"""
    current_datetime = str(datetime.now())

    request = ShareInfo()
    response_data = request.tickers_request()

    data = {"date": current_datetime, "quotes": response_data}

    serialized_data = pickle.dumps(data)

    return serialized_data


def main():
    """ Отправляет данные в redis"""

    serialized_data = data_conversion()
    redis_client.set(name='response_data', value=serialized_data)
    redis_client.close()


schedule.every(SURVEY_PERIOD).seconds.do(main)

while True:
    schedule.run_pending()
    time.sleep(1)
