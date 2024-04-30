# Import libraries
import json
from io import StringIO

import joblib
import pandas as pd
from flask import Flask, jsonify, request

app = Flask(__name__)

# Load the model
with open("model_test.joblib", "rb") as model_file:
    pipeline = joblib.load(model_file)


@app.route("/", methods=["POST"])
def predict():
    # Get the data from the POST request.
    data_json = request.get_json()
    data = data_json["data"]

    # Put the data in a dataframe and create features
    input_data = pd.DataFrame(data)
    input_data[["y", "lag1", "lag2"]] = pd.DataFrame(
        input_data["values"].tolist(), index=input_data.index
    )
    input_data = input_data.drop(columns="values")

    # Make prediction using model loaded from disk as per the data.
    preds_df = pd.DataFrame(
        pipeline.predict(input_data), index=input_data.index, columns=["lead1", "lead2"]
    )
    predictions = pd.concat([input_data.iloc[:, :2], preds_df], axis=1)
    # Reformat predictions in json
    predictions_json = predictions.to_json(orient="records", indent=4)
    output = json.dumps({"prediction": json.loads(predictions_json)}, indent=4)

    return jsonify(output)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
