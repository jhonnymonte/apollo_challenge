from flask import Flask, jsonify, request
import requests
import csv
import os
app = Flask(__name__)

@app.route("/createcsv", methods=["GET"])
def create_csv():
    
    list_packages = [
    'numpy',
    'pandas',
    'appnope',
    'asttokens',                
    'autopep8',                 
    'backcall',                 
    'cachetools',
    'requests',
    'setuptools',
    'urllib3',
    'pytz',
    'loguru',
    '3etool',
    'passwordly'            
]
    with open("packages.csv", "w", newline='') as file:
        
        for i in list_packages:
            response = requests.get(f"https://pypi.org/pypi/{i}/json").json()
            name = response['info']['name']
            downloads = response['info']['downloads']['last_month']
            python_version = response['info']['requires_python']
            last_version = response['info']['version']
            to_csv = [name,downloads,python_version,last_version]
            packages_list = csv.writer(file)
            packages_list.writerow(to_csv)

    return f'file create sucesfully'


@app.route('/packagename/<string:str_params>', methods=["GET"])
def package_list(str_params):
    data = []
    with open("./packages.csv") as file:
        csv_file = csv.reader(file)
        for row in csv_file:
            name = row[0]
            if str_params in name:
                data.append(row)
            return data
        


@app.route('/pythonversion/<string:str_params>', methods=["GET"])
def version_list(str_params):
    data = []
    with open("./packages.csv") as file:
        csv_file = csv.reader(file)
        for row in csv_file:
            python_version = row[2]
            if str_params in python_version:
                data.append(row)
            
        return data
        
@app.route('/all/', methods=["GET"])
def all_package():
    data = []
    with open("./packages.csv") as file:
        csv_file = csv.reader(file)
        for row in csv_file:
            data.append(row)
        return data



if __name__ == "__main__":
    
    app.run(debug=True)



