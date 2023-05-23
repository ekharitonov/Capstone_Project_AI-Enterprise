import pandas as pd
from flask import Flask, request, jsonify
from src.config import *
from src.model import model


app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/predict', methods=['POST'])
def predict():
    # Check date parameter in request
    if 'date' in request.args:
        date = request.args['date']
    else:
        return "Error: No date parameter was provided."
    # Check country parameter in request
    if 'country' in request.args:
        country = request.args['country']
    else:
        country = None
    # Check duration parameter in request
    if 'duration' in request.args:
        duration = request.args['duration']
        if duration == '':
            duration = 30
        else:
            duration = int(duration)
    else:
        duration = 30
    # Call model with parameters
    result = model(date, duration, country)
    # Return result
    return jsonify({
        'data': result
    })


@app.route('/logs', methods=['POST'])
def logs():
    if 'type' in request.args:
        type = request.args['type']
    else:
        return "Error: No type parameter was provided."
    if type == 'ingest':
        logs = pd.read_csv(DIRECTORY_LOGS + 'ingest.csv').to_dict()
    elif type == 'train':
        logs = pd.read_csv(DIRECTORY_LOGS + 'train.csv').to_dict()
    elif type == 'predict':
        logs = pd.read_csv(DIRECTORY_LOGS + 'predict.csv').to_dict()
    else:
        return "Error: Invalid type parameter was provided."
    return jsonify({
        'data': logs
    })
