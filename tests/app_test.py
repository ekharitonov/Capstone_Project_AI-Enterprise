import os, requests, unittest
from src.config import *

class AppTest(unittest.TestCase):

    def test_01_app_predict_country(self):
        baseUrl = APP_BASE_URL
        route = 'predict'
        date = '2018-11-20'
        duration = 30
        country = 'Australia'
        url = baseUrl + route + '?' \
        + 'date=' + date + '&' \
        + 'duration=' + str(duration) + '&' \
        + 'country=' + country
        response = requests.post(url)
        self.assertTrue('data' in response.json())

    def test_02_app_predict_total(self):
        baseUrl = APP_BASE_URL
        route = 'predict'
        date = '2018-11-20'
        duration = 30
        url = baseUrl + route + '?' \
        + 'date=' + date + '&' \
        + 'duration=' + str(duration)
        response = requests.post(url)
        self.assertTrue('data' in response.json())

    def test_03_app_logs(self):
        baseUrl = APP_BASE_URL
        route = 'logs'
        type = 'predict'
        url = baseUrl + route + '?' + 'type=' + type
        response = requests.post(url)
        self.assertTrue('data' in response.json())
