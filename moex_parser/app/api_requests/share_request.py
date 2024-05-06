"""Содержит класс для парсинга котировок акций с API MOEX"""
import requests


class ShareInfo():
    ''''
    Запрос списка котировок акций с API MOEX
    '''
    def tickers_request(self):
        '''
        Запрос к API MOEX котировального списка,
        возвращает список из пар(тикер:цена)
        '''
        response = requests.get("http://iss.moex.com/iss/engines/"
                                "stock/markets/shares/boards/TQBR/"
                                "securities.json?iss.meta=off&iss."
                                "only=marketdata&marketdata."
                                "columns=SECID,LAST", timeout=5).json()
        data = response['marketdata']['data']
        return data


request = ShareInfo()
response_data = request.tickers_request()
