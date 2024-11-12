#!/usr/bin/env python
from flask import Flask, jsonify, request

from pydub import AudioSegment
import os
import sqlite3

from DataManage import *
# from AI import predict

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False

@app.route('/')
def start():
    return "Hello World"

@app.route('/upload_audio', methods=['POST'])
def upload_audio():
    file = request.files['audio']
    
    upload_folder = './uploaded'

    file_path = os.path.join(upload_folder, file.filename)
    file.save(file_path)
    audio = AudioSegment.from_file(file_path, format="m4a")
    wavFilePath = file_path.replace("m4a", "wav")
    audio.export(wavFilePath, format="wav")
    prediction = predict(wavFilePath)
    
    os.remove(file_path)
    os.remove(wavFilePath)

    return jsonify({"probability": float(prediction)}), 200


# phone_number의 data_name 데이터 요청

@app.route('/get_data', methods=['POST'])
def get_data():
    phone_number = request.args.get('phone_number')
    print(phone_number)
    try:
        data = read(phone_number)
    except:
        initialize(phone_number)
        data = read(phone_number)
    print(type(data))
    return data, 200
    
@app.route('/add_percent', methods=['POST'])
def add_percent():
    phone_number = request.args.get('phone_number')
    percent = request.args.get('percent')
    print(type(percent))

    add_recent10(phone_number, float(percent))
    return "Data successfully updated", 200
#phone_number의 data_name 데이터 data_value로 업데이트

@app.route('/reported', methods=['POST'])
def reported():
    reporter = request.args.get('reporter')
    reported = request.args.get('reported')
    if isreported(reporter, reported):
        return "It already exist", 409
    reported1(reporter, reported)
    return "Data successfully updated", 200

@app.route('/detected', methods=['POST'])
def detected():
    phone_number = request.args.get('phone_number')

    detected1(phone_number)
    return "Data successfully updated", 200

@app.route('/update_data', methods=['POST'])
def update_data():
    phone_number = request.form['phone_number']
    data_name = request.form['data_name']
    data_value = request.form['data_value']

    update(phone_number, data_name, data_value)
    return "Data successfully updated", 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
