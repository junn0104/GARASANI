#!/usr/bin/env python
import json

data_path = './data'

init_data = {"reported_count": 0, "received_reports_count": 0, "tested_count": 0, "received_tests_count": 0, "ai_detected_count": 0}


def initialize(number):
    try:
        open(f'{data_path}/{number}.json', 'r')
    except:
        with open(f'{data_path}/{number}.json', 'w') as f:
            json.dump(init_data, f, indent=4)

def read(number):
    with open(f'{data_path}/{number}.json', 'r') as f:
        data = json.load(f)
    return data

def update(number, data_name, data_value):
    with open(f'{data_path}/{number}.json', 'r') as f:
        data = json.load(f)
    data[data_name] = data_value
    with open(f'{data_path}/{number}.json', 'w') as f:
        json.dump(data, f, indent=4)
