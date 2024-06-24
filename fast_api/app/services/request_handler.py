"""
Модуль содержит функции для опроса redis и обработки полученных данных
"""
import pickle
import redis


redis_client = redis.Redis(host='redis', port='6379')


def data_request():
    """Забирает сериализованноые данные
    с redis, отправленные парсером"""
    serialized_data = redis_client.get('response_data')
    redis_client.close()
    return serialized_data


def data_deserializing():
    """Десериализует полученные данные"""
    deserialized_data = pickle.loads(data_request())
    return deserialized_data


def loading_data():
    """Отдача обработанных данных"""
    return data_deserializing()
