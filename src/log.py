import csv, os, uuid
from datetime import datetime
from src.config import VERSION, DIRECTORY_LOGS


def log_common(log_file, log_data, headers, directory_logs):
    header=False
    if not os.path.exists(directory_logs):
        os.makedirs(directory_logs)
    if not os.path.exists(directory_logs + log_file):
        header = True
    with open(directory_logs + log_file, 'a', newline='') as file:
        writer = csv.writer(file)
        if header:
            writer.writerow(headers)
        writer.writerow(log_data)


def log_ingest(shape):
    now = datetime.now()
    id = str(uuid.uuid4())[:8]
    log_file = 'ingest.csv'
    log_data = list(map(str, [id, now, shape]))
    headers = ['id', 'time', 'shape']
    log_common(log_file, log_data, headers, DIRECTORY_LOGS)


def log_train(model, shape, performance, version=VERSION):
    now = datetime.now()
    id = str(uuid.uuid4())[:8]
    log_file = 'train.csv'
    log_data = list(map(str, [id, now, version, model, shape, performance]))
    headers = ['id', 'time', 'version', 'model', 'shape', 'performance']
    log_common(log_file, log_data, headers, DIRECTORY_LOGS)


def log_predict(model, query, prediction, version=VERSION):
    now = datetime.now()
    id = str(uuid.uuid4())[:8]
    log_file = 'predict.csv'
    log_data = list(map(str, [id, now, version, model, query, prediction]))
    headers = ['id', 'time', 'version', 'model', 'query', 'prediction']
    log_common(log_file, log_data, headers, DIRECTORY_LOGS)
