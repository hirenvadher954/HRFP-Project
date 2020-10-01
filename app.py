from flask import Flask, request, jsonify, render_template
from flask_restful import Api, Resource
import model
import pyrebase


app = Flask(__name__)
api = Api(app)
#'time','ejection_fraction','serum_creatinine','age'


@app.route("/predict", methods=['POST'])
def predict():
    data = request.get_json()
    print(type(data))
    features = [float(x) for x in data.values()]
    print(type(request.form))
    return model.predict(features)


if __name__ == "__main__":
    app.run(debug=True)
