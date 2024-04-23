import csv

from flask import Flask, jsonify, render_template, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Added the UTF encoding because there was a hidden character preventing the first column from mapping
def load_data_from_csv(file_path):
    data = []
    with open(file_path, 'r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/data')
def get_data():
    # Get filter parameters from query string
    document_label = request.args.get('documentLabel')
    int_label = request.args.get('intLabel')
    att_label = request.args.get('attLabel')
    prop_name = request.args.get('attributeDictionaryPropName')
    table = request.args.get('table')

    # Load data from CSV file
    data = load_data_from_csv('data.csv')

    # Filter data based on query parameters
    filtered_data = data
    if document_label:
        filtered_data = [row for row in filtered_data if document_label.lower() in row['documentLabel'].lower()]
    if int_label:
        filtered_data = [row for row in filtered_data if int_label.lower() in row['intLabel'].lower()]
    if att_label:
        filtered_data = [row for row in filtered_data if att_label.lower() in row['attLabel'].lower()]
    if prop_name:
        filtered_data = [row for row in filtered_data if prop_name.lower() in row['attributeDictionaryPropName'].lower()]
    if table:
        filtered_data = [row for row in filtered_data if table.lower() in row['table'].lower()]

    filtered_data = sorted(filtered_data, key=lambda x: x['documentLabel'])
    return jsonify(filtered_data)

if __name__ == '__main__':
    app.run()

