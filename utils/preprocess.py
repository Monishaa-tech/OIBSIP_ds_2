def preprocess_input(year, km, fuel):
    fuel_map = {'Petrol': 0, 'Diesel': 1, 'CNG': 2}

    try:
        year = int(year)
        km = int(km)
        fuel_val = fuel_map[fuel]

        return [[year, km, fuel_val]]

    except:
        return None