from flask import Flask, request, jsonify, render_template
from flask_restful import Api, Resource
import model


app = Flask(__name__)
api = Api(app)
#'time','ejection_fraction','serum_creatinine','age'


@app.route("/predict", methods=['POST'])
def predict():
    features = [float(x) for x in request.form.values()]
    return model.predict(features)


if __name__ == "__main__":
    app.run(debug=True)
