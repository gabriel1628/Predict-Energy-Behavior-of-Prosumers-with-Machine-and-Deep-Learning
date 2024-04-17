# Import libraries
import joblib
import pandas as pd
from flask import Flask, jsonify, request

app = Flask(__name__)

# Load the model
# with open('model_test.joblib', 'rb') as model_file:
#     pipeline = joblib.load(model_file)

@app.route('/',methods=['POST'])
def predict():
    # Get the data from the POST request.
    data = request.get_json(force=True)

    # Make prediction using model loaded from disk as per the data.
    

    # return jsonify(output)
    return jsonify(data)


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)