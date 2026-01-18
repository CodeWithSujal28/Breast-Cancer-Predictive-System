from flask import Flask, render_template, request
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load saved files
model = joblib.load("breast_cancer_model.pkl")
scaler = joblib.load("scaler.pkl")
selector = joblib.load("feature_selector.pkl")

# Feature names (same order as selected)
feature_names = selector.get_feature_names_out()

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None

    if request.method == "POST":
        values = [float(request.form[f]) for f in feature_names]
        input_df = pd.DataFrame([values], columns=feature_names)

        input_scaled = scaler.transform(input_df)
        result = model.predict(input_scaled)[0]

        prediction = "Benign (Not Cancerous)" if result == 1 else "Malignant (Cancerous)"

    return render_template(
        "index.html",
        prediction=prediction,
        feature_names=feature_names
    )

if __name__ == "__main__":
    app.run(debug=True)
