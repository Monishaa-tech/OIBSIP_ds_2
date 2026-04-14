import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

data = {
    'year': [2015, 2018, 2020, 2012, 2016, 2022, 2019],
    'km': [50000, 30000, 20000, 90000, 60000, 15000, 25000],
    'fuel': [0, 1, 0, 1, 2, 0, 1],
    'price': [300000, 500000, 700000, 200000, 400000, 800000, 600000]
}

df = pd.DataFrame(data)

X = df[['year', 'km', 'fuel']]
y = df['price']

model = LinearRegression()
model.fit(X, y)

pickle.dump(model, open('model/model.pkl', 'wb'))

print("Model trained successfully!")