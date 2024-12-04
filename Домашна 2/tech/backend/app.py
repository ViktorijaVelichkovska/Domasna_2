import os
import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)


#endpoint
@app.route('/api/company/<company_name>', methods=['GET'])
@app.route('/')
def home():
    return "Добредојдовте на Македонската Берза!"

def get_company_data(company_name):
    try:
        #proverka dali fileot postoi vo all_data/
        file_path = f'all_data/{company_name}.csv'


        print(f"Looking for file at: {file_path}")


        if os.path.exists(file_path):
            data = pd.read_csv(file_path)

            data = data.fillna(0)
            return jsonify(data.to_dict(orient='records'))  # Враќа податоци како JSON
        else:
            return jsonify({"error": f"{company_name}.csv not found"}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# endpoint za site kompanii
@app.route('/api/companies', methods=['GET'])
def get_companies():
    # site csv files od all_data
    company_files = [f.replace('.csv', '') for f in os.listdir('all_data') if f.endswith('.csv')]

    #lista na iminja na kompanii
    return jsonify(company_files)


if __name__ == '__main__':
    app.run(debug=True)
