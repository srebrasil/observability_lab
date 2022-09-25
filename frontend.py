from flask import Flask, jsonify
import requests
import random
from classes.Metrics import Metrics

metrics = Metrics("localhost", 8000)
app_metrics = metrics.collect_metrics("frontend")


app = Flask(__name__)

operations = ['sum', 'sub', 'mult', 'div']
ports = {'v1': 4001, 'v2': 4002, 'v3': 4003}
 

@app.route('/api/v1/frontend', methods=['GET'])
def get_test():
    response = requests.get('http://localhost:'+str(random.choice(list(ports.values())))+'/api/v1/calc/'+ random.choice(operations) +'/' + str(random.randint(1, 1000)) + '/' + str(random.randint(1, 1000)))
    if response.status_code == 200:
        combined_response = requests.get('http://localhost:'+str(random.choice(list(ports.values())))+'/api/v1/calc/'+ random.choice(operations) +'/' + str(random.randint(1, 1000)) + '/' + str(random.randint(1, 1000)))
    return jsonify({'Result1' : response.json()['result'], 'Result2' : combined_response.json()['result']})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4000)