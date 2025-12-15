from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import joblib
import numpy as np

app = FastAPI()

# Load model
model = joblib.load(r"C:\Users\Pc Planet\Downloads\Uni\sem 5\ML\project\model.pkl")

# Home page with input form
@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <body>
            <h2>Stock Prediction</h2>
            <form action="/predict" method="post">
                Open: <input type="number" step="any" name="Open"><br><br>
                High: <input type="number" step="any" name="High"><br><br>
                Low: <input type="number" step="any" name="Low"><br><br>
                Close: <input type="number" step="any" name="Close"><br><br>
                Volume: <input type="number" step="any" name="Volume"><br><br>
                <button type="submit">Predict</button>
            </form>
        </body>
    </html>
    """

# Prediction route
@app.post("/predict", response_class=HTMLResponse)
def predict(
    Open: float = Form(...),
    High: float = Form(...),
    Low: float = Form(...),
    Close: float = Form(...),
    Volume: float = Form(...)
):
    data = np.array([[Open, High, Low, Close, Volume]])
    result = model.predict(data)[0]

    prediction = "STOCK WILL GO UP 📈" if result == 1 else "STOCK WILL GO DOWN 📉"

    return f"""
    <html>
        <body>
            <h2>{prediction}</h2>
            <a href="/">Go Back</a>
        </body>
    </html>
    """
