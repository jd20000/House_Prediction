from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model and scaler
with open("model/house_price_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("model/scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

@app.route("/", methods=["GET", "POST"])
def predict():
    prediction = None
    error_message = None
    if request.method == "POST":
        try:
            # Get input values
            medinc = float(request.form["medinc"])
            house_age = float(request.form["house_age"])
            avg_rooms = float(request.form["avg_rooms"])
            avg_occup = float(request.form["avg_occup"])

            # **Back-end validation**
            if medinc <= 0:
                error_message = "Median income must be a positive number."
            elif house_age < 0 or house_age > 150:
                error_message = "House age must be between 0 and 150 years."
            elif avg_rooms <= 0:
                error_message = "Average rooms must be greater than zero."
            elif avg_occup <= 0:
                error_message = "Average occupancy must be greater than zero."

            if error_message:
                return render_template("index.html", prediction=None, error_message=error_message)

            # Transform input data
            input_features = np.array([[medinc, house_age, avg_rooms, avg_occup]])
            input_scaled = scaler.transform(input_features)

            # Modify this line in app.py
            predicted_price = model.predict(input_scaled)[0] * 100000  # Multiply by 1 lakh
            prediction = f"₹{predicted_price:,.2f}"  # Format as Indian Rupees


        except Exception as e:
            prediction = "Invalid input. Please try again."

    return render_template("index.html", prediction=prediction, error_message=error_message)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
