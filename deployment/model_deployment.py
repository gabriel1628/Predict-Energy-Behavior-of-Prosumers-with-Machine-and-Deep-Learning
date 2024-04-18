# Import libraries
from io import StringIO

import joblib
import pandas as pd
from flask import Flask, jsonify, request

app = Flask(__name__)

# to drop 'unique_id' and 'ds' columns from X when using fit and predict
class columnDropperTransformer():
    def __init__(self, columns):
        self.columns = columns

    def transform(self, X, y=None):
        return X.drop(self.columns, axis=1)

    def fit(self, X, y=None):
        return self
    

# Load the model
with open('model_test.joblib', 'rb') as model_file:
    pipeline = joblib.load(model_file)

@app.route('/',methods=['POST'])
def predict():
    # Get the data from the POST request.
    data_json = request.get_json()

    # Make prediction using model loaded from disk as per the data.
    input_data = pd.DataFrame(data_json)
    input_data[["y", "lag1", "lag2"]] = pd.DataFrame(input_data["values"].tolist(), index= input_data.index)
    input_data = input_data.drop(columns="values")
    preds_df = pd.DataFrame(pipeline.predict(input_data), index=input_data.index, columns=["lead1", "lead2"])
    predictions = pd.concat(
        [input_data.iloc[:, :2], preds_df],
        axis=1
    )

    output = predictions.to_json(orient="records", indent=4)

    return jsonify(output)


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)