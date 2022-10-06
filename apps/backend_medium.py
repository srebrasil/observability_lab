
# import flask and jsonify
from flask import Flask, jsonify
#expose endpoint to return the operation of class Calc
from classes.Calc import Calc
from random import randint
from time import sleep
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)
metrics.info('app_info', 'Application info', version='1.0.0', app_name='backend-medium')

@app.route('/api/v1/calc/sum/<int:num1>/<int:num2>', methods=['GET']) # route to expose the api
def get_sum(num1, num2):
    sleep(randint(1, 5))
    calc = Calc(num1, num2)
    return jsonify({'result': calc.sum()})

@app.route('/api/v1/calc/sub/<int:num1>/<int:num2>', methods=['GET']) # route to expose the api
def get_sub(num1, num2):
    sleep(randint(1, 5))
    calc = Calc(num1, num2)
    return jsonify({'result': calc.sub()})

@app.route('/api/v1/calc/mult/<int:num1>/<int:num2>', methods=['GET']) # route to expose the api
def get_mult(num1, num2):
    sleep(randint(1, 5))
    calc = Calc(num1, num2)
    return jsonify({'result': calc.mult()})

@app.route('/api/v1/calc/div/<int:num1>/<int:num2>', methods=['GET']) # route to expose the api
def get_div(num1, num2):
    sleep(randint(1, 5))
    calc = Calc(num1, num2)
    return jsonify({'result': calc.div()})

if __name__ == '__main__': # run the app
    app.run(debug=True, host='0.0.0.0', port='4002') # run the app
