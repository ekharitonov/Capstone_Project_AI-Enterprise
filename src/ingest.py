import os, re
import numpy as np
import pandas as pd
from tqdm import tqdm
from src.config import *
from src.log import log_ingest


def get_data(keys, key_names, directory_data, directory_output):
    ''' Read source data into a tabular data structure '''
    # Initialise dataframe with desired column names
    data = pd.DataFrame(columns=keys, dtype=int)
    for file_name in tqdm(os.listdir(directory_data)):
        with open(directory_data + file_name) as file:
            # Read JSON into pandas dataframe
            transactions = pd.read_json(file)
        # Rename column names using desired mappings
        transactions.rename(columns=key_names, inplace=True)
        # Concatenate transactions from file to master dataframe
        data = pd.concat([data, transactions])
    # Persist transactions in CSV file
    data.to_csv(directory_output+'0 data.csv', index=False)
    return data


def clean_data(data, keys, key_types, directory_output):
    ''' Transform data into a cleaned dataframe '''
    data = data.copy()
    # Remove duplicate rows
    data.drop_duplicates(inplace=True)
    # Replace null with -1
    data.fillna(value=-1, inplace=True)
    # Some features have non-numeric characters; remove those characters from string
    data['invoice_id'] = data['invoice_id'].apply(lambda x: re.sub("[^0-9]", "", x))
    data['stream_id'] = data['stream_id'].apply(lambda x: re.sub("[^0-9]", "", x))
    # Replace empty strings with -1
    data = data.replace(r'^\s*$', -1, regex=True)
    # Update data types to reduce memory consumption
    for key in keys:
        data[key] = data[key].astype(key_types[key])
    # Persist cleaned transactions in CSV file
    data.to_csv(directory_output+'1 data_cleaned.csv', index=False)
    return data


def prepare_data(data, directory_output):
    ''' Perform feature transformations to prepare data for model '''
    data = data.copy()
    # Generate date from time-related features
    data['date'] = pd.to_datetime(data[['year', 'month', 'day']])
    # Remove time-related features once date has been generated
    data.drop(['year', 'month', 'day'], axis=1, inplace=True)
    # Remove nominal features containing IDs
    data.drop(['invoice_id', 'customer_id', 'stream_id'], axis=1, inplace=True)
    # Remove negative price rows
    data = data[data['price'] > 0]
    # Remove excessively expensive transactions
    #data = data[data['price'] < 1000]
    # Persist prepared features in CSV file
    data.to_csv(directory_output+'2 data_engineered.csv', index=False)
    return data


def calculate_revenue_country(data, directory_output):
    ''' Aggregate individual transactions into daily revenue by country '''
    # Sum transaction prices by country and date
    revenue = data \
        .groupby(['country', 'date'])['price'] \
        .sum() \
        .reset_index()
    revenue.rename(columns={'price': 'revenue'}, inplace=True)
    # Persist calculated daily revenue by country in CSV file
    revenue.to_csv(directory_output+'3 revenue_country.csv', index=False)
    return None


def calculate_revenue_total(data, directory_output):
    ''' Aggregate individual transactions into daily total revenue '''
    # Sum transaction prices by date
    revenue = data \
        .groupby(['date'])['price'] \
        .sum() \
        .reset_index()
    revenue.set_index('date', inplace=True)
    revenue.rename(columns={'price': 'revenue'}, inplace=True)
    # Persist calculated daily total revenue in CSV file
    revenue.to_csv(directory_output+'4 revenue_total.csv')
    return None


def ingest(force=False):
    if not os.path.exists(DIRECTORY_OUTPUT):
        os.makedirs(DIRECTORY_OUTPUT)
    if force or not os.path.exists(DIRECTORY_OUTPUT+'4 revenue_total.csv'):
        print('Reading data...')
        data = get_data(keys, key_names, DIRECTORY_INPUT, DIRECTORY_OUTPUT)
        print('Cleaning data...')
        data = clean_data(data, keys, key_types, DIRECTORY_OUTPUT)
        print('Preparing features...')
        data = prepare_data(data, DIRECTORY_OUTPUT)
        print('Calculating revenue by country...')
        calculate_revenue_country(data, DIRECTORY_OUTPUT)
        print('Calculating total revenue...')
        calculate_revenue_total(data, DIRECTORY_OUTPUT)
        print('Done.')
        log_ingest(data.shape)
