from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load trained model
model = joblib.load(r'C:\Users\Pc Planet\Downloads\Uni\sem 5\ML\project\model.pkl')

# EXACT features (same as Gradio)
features = ['Open', 'High', 'Low', 'Close', 'Volume']

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None

    if request.method == "POST":
        values = []

        for feature in features:
            values.append(float(request.form[feature]))

        final_input = np.array(values).reshape(1, -1)
        result = model.predict(final_input)[0]

        prediction = "STOCK WILL GO UP 📈" if result == 1 else "STOCK WILL GO DOWN 📉"

    return render_template(
        "index.html",
        features=features,
        prediction=prediction
    )

if __name__ == "__main__":
    app.run(debug=True)
