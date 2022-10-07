from flask import Flask, jsonify
import requests
import random
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)
metrics.info('app_info', 'Application info', version='1.0.0', app_name='frontend')

operations = ['sum', 'sub', 'mult', 'div']
ports = {'v1': 'http://backend_fast:4001', 'v2': 'http://backend_medium:4002', 'v3': 'http://backend_slow:4003'}
 

@app.route('/api/v1/frontend', methods=['GET'])
def get_test():
    response = requests.get(str(random.choice(list(ports.values())))+'/api/v1/calc/'+ random.choice(operations) +'/' + str(random.randint(1, 1000)) + '/' + str(random.randint(1, 1000)))
    if response.status_code == 200:
        combined_response = requests.get(str(random.choice(list(ports.values())))+'/api/v1/calc/'+ random.choice(operations) +'/' + str(random.randint(1, 1000)) + '/' + str(random.randint(1, 1000)))
    return jsonify({'Result1' : response.json()['result'], 'Result2' : combined_response.json()['result']})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4000)