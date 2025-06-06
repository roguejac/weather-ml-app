import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

MODEL_FILE = "model.pkl"
DATA_FILE = "weather_data.csv"

def train_model():
    if not os.path.exists(DATA_FILE):
        return

    df = pd.read_csv(DATA_FILE)
    df['label'] = df['temp'].apply(lambda x: 1 if x > 20 else 0)
    X = df[['temp', 'humidity']]
    y = df['label']

    model = RandomForestClassifier()
    model.fit(X, y)

    joblib.dump(model, MODEL_FILE)

def predict(temp, humidity):
    if not os.path.exists(MODEL_FILE):
        return "Model not trained"

    model = joblib.load(MODEL_FILE)
    prediction = model.predict([[temp, humidity]])[0]
    return "Hot" if prediction == 1 else "Cold"

def save_weather_data(weather):
    df_new = pd.DataFrame([weather])
    if os.path.exists(DATA_FILE):
        df_existing = pd.read_csv(DATA_FILE)
        df_combined = pd.concat([df_existing, df_new], ignore_index=True)
    else:
        df_combined = df_new
    df_combined.to_csv(DATA_FILE, index=False)