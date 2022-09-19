# function to expose a rest api to return a json object with date and time GMT-3

from flask import Flask, jsonify # import flask and jsonify
from datetime import datetime, timedelta # import datetime and timedelta

app = Flask(__name__) # create the Flask app

@app.route('/api/v1/time', methods=['GET']) # route to expose the api
def get_time(): # function to return a json object with date and time GMT-3
    time = datetime.now() - timedelta(hours=3)  # GMT-3
    return jsonify({'time': time.strftime('%Y-%m-%d %H:%M:%S')}) # return json object


if __name__ == '__main__': # run the app
    app.run(debug=True, host='0.0.0.0', port='4000') # run the app
