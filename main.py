#!/usr/bin/env python
from flask import Flask, request

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

# @app.route('/upload_audio', methods=['POST'])
# def upload_audio():
#     file = request.files['audio']
#    
#     upload_folder = './uploaded'

#     file_path = os.path.join(upload_folder, file.filename)
#     file.save(file_path)
#     audio = AudioSegment.from_file(file_path, format="m4a")
#     wavFilePath = file_path.replace("m4a", "wav")
#     audio.export(wavFilePath, format="wav")
#     prediction = predict(wavFilePath)
    
#     os.remove(file_path)
#     os.remove(wavFilePath)

#     return f"File was detected as {prediction}", 200

@app.route('/get_data', methods=['POST'])
def get_data():
    phone_number = request.form['phone_number']
    data_name = request.form['data_name']
    data = read(phone_number)
    return str(data[data_name]), 200
    

@app.route('/update_data', methods=['POST'])
def update_data():
    phone_number = request.form['phone_number']
    data_name = request.form['data_name']
    data_value = request.form['data_value']

    update(phone_number, data_name, data_value)
    return "Data successfully updated", 200


@app.route('/make_data', methods=['POST'])
def make_data():
    phone_number = request.form['phone_number']
    data_name = request.form['data_name']
    data_value = request.form['data_value']
    
    # create(phone_number, data_name, data_value)
    
    return "Data successfully created", 200




if __name__ == '__main__':
    app.run(host="0.0.0.0", port="1994")
