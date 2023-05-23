import os, unittest
from src.config import *
from src.model import model

class ModelTest(unittest.TestCase):

    def test_01_model_train(self):
        model_file = DIRECTORY_MODELS + 'arima.pickle'
        date = '2018-11-20'
        duration = 30
        country = None
        model(date, duration, country)
        self.assertTrue(os.path.exists(model_file))

    def test_02_model_predict(self):
        key = 'arima'
        date = '2018-11-20'
        duration = 30
        country = None
        result = model(date, duration, country)
        self.assertTrue(key in result)
