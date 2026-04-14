import pickle

model = pickle.load(open('model/model.pkl', 'rb'))

def predict_price(data):
    try:
        price = model.predict(data)[0]

        # Fix range
        price = max(100000, min(abs(price), 1000000))

        return int(price)

    except:
        return None