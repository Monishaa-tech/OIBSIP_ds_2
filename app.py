from flask import Flask, render_template, request
from utils.preprocess import preprocess_input
from utils.predict import predict_price
from utils.explain import generate_explanation

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


# 🔵 SINGLE PREDICTION
@app.route('/predict', methods=['POST'])
def predict():
    try:
        year = request.form['year']
        km = request.form['km']
        fuel = request.form['fuel']

        data = preprocess_input(year, km, fuel)

        if data is None:
            return render_template('index.html',
                                   prediction_text="⚠ Invalid Input")

        price = predict_price(data)
        reasons = generate_explanation(int(year), int(km))

        return render_template('index.html',
                               prediction_text=f"₹ {price}",
                               reasons=reasons)

    except:
        return render_template('index.html',
                               prediction_text="⚠ Error occurred")


# 🔴 COMPARE
@app.route('/compare', methods=['POST'])
def compare():
    try:
        data_a = preprocess_input(
            request.form['year_a'],
            request.form['km_a'],
            request.form['fuel_a']
        )

        data_b = preprocess_input(
            request.form['year_b'],
            request.form['km_b'],
            request.form['fuel_b']
        )

        price_a = predict_price(data_a)
        price_b = predict_price(data_b)

        better = "Car A offers better value 🚗" if price_a > price_b else "Car B offers better value 🚗"

        return render_template('index.html',
                               price_a=price_a,
                               price_b=price_b,
                               better=better)

    except:
        return render_template('index.html',
                               better="⚠ Comparison failed")


if __name__ == "__main__":
    app.run(debug=True)