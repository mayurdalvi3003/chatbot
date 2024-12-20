import json
import os

def load_json_data():
    data_dir = os.path.join(os.path.dirname(__file__), 'data')
    json_files = ['Economy_Class_Updated.json', 'Business_Class_Updated.json', 'First_Class_Updated.json']
    data = {}
    for file_name in json_files:
        with open(os.path.join(data_dir, file_name), 'r') as f:
            data[file_name.split('.')[0]] = json.load(f)
    return data
