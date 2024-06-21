import pickle
import numpy as np
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load the saved AdaBoost model from the file
model_filename = 'model.pkl'
with open(model_filename, 'rb') as file:
    loaded_adb = pickle.load(file)

# Function to convert prediction output to 'fail' or 'success'
def convert_prediction(prediction):
    return 'success' if prediction == 1 else 'fail'

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    user_input = np.array(data).reshape(1, -1)
    prediction = loaded_adb.predict(user_input)
    prediction_label = convert_prediction(prediction[0])
    return jsonify({'prediction': prediction_label})

if __name__ == '__main__':
    app.run(debug=True)
