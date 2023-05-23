import os, unittest
from src.config import *
from src.log import log_ingest, log_train, log_predict

class LogTest(unittest.TestCase):

    def test_01_log_ingest(self):
        log_file = DIRECTORY_LOGS + 'ingest.csv'
        shape = (1000, 10)
        log_ingest(shape)
        self.assertTrue(os.path.exists(log_file))

    def test_02_log_train(self):
        log_file = DIRECTORY_LOGS + 'train.csv'
        model = 'test'
        shape = (1000, 10)
        performance = {'metric': 0.5}
        log_train(model, shape, performance)
        self.assertTrue(os.path.exists(log_file))

    def test_03_log_predict(self):
        log_file = DIRECTORY_LOGS + 'predict.csv'
        model = 'test'
        query = {
            'date': '2020-01-01',
            'duration': 30,
            'country': 'Australia'
        }
        prediction = {'label': 1}
        log_predict(model, query, prediction)
        self.assertTrue(os.path.exists(log_file))
