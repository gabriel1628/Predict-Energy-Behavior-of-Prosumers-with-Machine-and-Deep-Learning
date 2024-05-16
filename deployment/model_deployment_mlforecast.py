# Import libraries
import json

import joblib
import pandas as pd
from flask import Flask, jsonify, request

app = Flask(__name__)

# Load the model
with open("model_mlforecast.joblib", "rb") as model_file:
    model = joblib.load(model_file)


@app.route("/", methods=["GET"])
def home_endpoint():
    return "Welcome to the homepage ! To get your energy forecasts, send your data to the /predict endpoint"


@app.route("/api/predict", methods=["GET"])
def predict_endpoint():
    return jsonify({"connection": "OK"})


@app.route("/api/predict", methods=["POST"])
def predict():
    # Get the data from the POST request.
    data_json = request.get_json()
    data = data_json["data"]

    # Put the data in a dataframe and create features
    input_data = pd.DataFrame(data)
    datetimes = input_data.drop(columns=["consumption"])
    input_data["datetime"] = pd.to_datetime(input_data["datetime"])

    # Make prediction using model loaded from disk as per the data.
    model.update(input_data)
    predictions = model.predict(24)
    output = []
    for building_id in predictions["building_id"].unique():
        try:
            output.append(
                {
                    "building_id": int(building_id),
                    "datetime": datetimes.loc[
                        datetimes["building_id"] == building_id, "datetime"
                    ].values[0],
                    "forecasts": predictions.loc[
                        predictions["building_id"] == building_id, "model"
                    ].to_list(),
                }
            )
        except:
            output.append(
                {
                    "building_id": int(building_id),
                    "datetime": None,
                    "forecasts": predictions.loc[
                        predictions["building_id"] == building_id, "model"
                    ].to_list(),
                }
            )
    output = {"predictions": output}
    output = json.dumps(output, indent=4)

    return jsonify(output)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
