from flask import Flask, request, jsonify
import pickle
import numpy as np


# 🚀 Load the model
with open("titanic_model.pkl", "rb") as file:
    model = pickle.load(file)

app = Flask(__name__)

@app.route('/')
def home():
    return "Titanic Survival Predictor is LIVE! 🚢"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()  # 🔍 Expects JSON input
    features = np.array([data['features']])  # 👈 Make sure input is a list
    prediction = model.predict(features)
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)
