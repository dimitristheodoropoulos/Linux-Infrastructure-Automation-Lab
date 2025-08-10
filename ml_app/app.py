# /home/testuser/Linux-Infrastructure-Automation-Lab/ml_app/app.py

import numpy as np
import joblib
from sklearn.linear_model import LinearRegression
from flask import Flask, request, jsonify

# --- Model Training and Saving (runs once on startup) ---
# Sample data
X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
y = np.dot(X, np.array([1, 2])) + 3

# Train a simple model
model = LinearRegression().fit(X, y)

# Save the trained model to a file
joblib.dump(model, 'model.joblib')
print("Model trained and saved as model.joblib")

# --- Flask Application (runs continuously) ---
# Create the Flask application instance
app = Flask(__name__)

# Load the trained model from the file
try:
    loaded_model = joblib.load('model.joblib')
    print("Model loaded successfully.")
except FileNotFoundError:
    print("Error: model.joblib not found. Ensure the training script ran first.")
    loaded_model = None

@app.route('/')
def home():
    """A simple home page to confirm the app is running."""
    return "ML App is running! Use the /predict endpoint to make predictions."

@app.route('/predict', methods=['POST'])
def predict():
    """
    Predicts the output based on the input JSON data.
    Input JSON should be of the format: {"data": [[x1, y1], [x2, y2]]}
    """
    if loaded_model is None:
        return jsonify({"error": "Model not loaded"}), 500
    
    data = request.json.get('data')
    if not data:
        return jsonify({"error": "No data provided"}), 400
    
    try:
        input_data = np.array(data)
        predictions = loaded_model.predict(input_data)
        return jsonify({"predictions": predictions.tolist()})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    # This block is for local development and will not be used by gunicorn
    app.run(host='0.0.0.0', port=5000, debug=True)
