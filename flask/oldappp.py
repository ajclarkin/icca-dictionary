import csv
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

#Sample data (replace with your actual data source)
# data = [
#     {'documentid': 1, 'documentName': 'Document 1', 'fieldid': 'field1', 'fieldName': 'Field 1'},
#     {'documentid': 1, 'documentName': 'Document 1', 'fieldid': 'field2', 'fieldName': 'Field 2'},
#     {'documentid': 2, 'documentName': 'Document 2', 'fieldid': 'field3', 'fieldName': 'Field 3'},
#     {'documentid': 2, 'documentName': 'Document 2', 'fieldid': 'field4', 'fieldName': 'Field 4'},
#     {'documentid': 3, 'documentName': 'Document 3', 'fieldid': 'field5', 'fieldName': 'Field 5'},
#  ]
def load_data_from_csv(file_path):
    data = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data



@app.route('/api/data')
def get_data():
    # Get filter parameters from query string
    documentid = request.args.get('documentid')
    document_name = request.args.get('documentName')
    field_name = request.args.get('fieldName')

    # Load data from CSV file
    data = load_data_from_csv('data.csv')

    # Filter data based on query parameters
    filtered_data = data
    if documentid:
        filtered_data = [row for row in filtered_data if str(row['documentid']) == documentid]
    if document_name:
        filtered_data = [row for row in filtered_data if document_name.lower() in row['documentName'].lower()]
    if field_name:
        filtered_data = [row for row in filtered_data if field_name.lower() in row['fieldName'].lower()]

    return jsonify(filtered_data)

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()

