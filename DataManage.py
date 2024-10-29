#!/usr/bin/env python
import json

data_path = './data'

init_data = {
    "phone_number": "",
    "reported_count": 0,
    "ai_detected_count": 0,
    "recent10_percent": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
}

def initialize(number):
    try:
        open(f'{data_path}/{number}.json', 'r')
    except:
        with open(f'{data_path}/{number}.json', 'w') as f:
            x=init_data
            init_data['phone_number']=number
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

def add_recent10(number, data_value):
    with open(f'{data_path}/{number}.json', 'r') as f:
        data = json.load(f)
    data["recent10_percent"].append(data_value)
    data["recent10_percent"].pop(0)
    with open(f'{data_path}/{number}.json', 'w') as f:
        json.dump(data, f, indent=4)

def reported1(reporter, reported):
    with open(f'{data_path}/{reported}.json', 'r') as f:
        data = json.load(f)
    data["reported_count"]+=1
    with open(f'{data_path}/{reported}.json', 'w') as f:
        json.dump(data, f, indent=4)
    with open(f'{data_path}/reported.json', 'r') as f:
        data = json.load(f)
    new_report = {
        "reporter": reporter,
        "reported": reported
    }
    data.append(new_report)
    with open(f'{data_path}/reported.json', 'w') as f:
        json.dump(data, f, indent=4)

def detected1(number):
    with open(f'{data_path}/{number}.json', 'r') as f:
        data = json.load(f)
    data["ai_detected_count"]+=1
    with open(f'{data_path}/{number}.json', 'w') as f:
        json.dump(data, f, indent=4)

def isreported(reporter, reported):
    with open(f'{data_path}/reported.json', 'r') as f:
        data = json.load(f)
    for report in data:
        if report["reporter"] == reporter and report["reported"] == reported:
            return True
    return False
