import csv
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)


class Intervention(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    documentLabel = db.Column(db.String(100))
    intLabel = db.Column(db.String(100))
    attributeDictionaryPropName = db.Column(db.String(100))
    table = db.Column(db.String(100))



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/data')
def get_data():
    # Get filter parameters from query string
    document_label = request.args.get('documentLabel')
    int_label = request.args.get('intLabel')
    prop_name = request.args.get('attributeDictionaryPropName')
    table = request.args.get('table')


    # Query the database based on filter parameters
    interventions = Intervention.query
    if document_label:
        interventions = interventions.filter(Intervention.documentLabel.ilike(f'%{document_label}%'))
    if int_label:
        interventions = interventions.filter(Intervention.intLabel.ilike(f'%{int_label}%'))
    if prop_name:
        interventions = interventions.filter(Intervention.attributeDictionaryPropName.ilike(f'%{prop_name}%'))
    if table:
        interventions = interventions.filter(Intervention.table.ilike(f'%{table}%'))

    # Convert the results to a list of dictionaries
    data = [
        {
            'documentLabel': intervention.documentLabel,
            'intLabel': intervention.intLabel,
            'attributeDictionaryPropName': intervention.attributeDictionaryPropName,
            'table': intervention.table
        }
        for intervention in interventions
    ]

    return jsonify(filtered_data)

if __name__ == '__main__':
    app.run()

