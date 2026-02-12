import random
import time
import requests
import json
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score # for checking model quality
from sklearn.model_selection import train_test_split

# Replace with your free OpenWeatherMap API key
API_KEY = '061b8234f273f7a8d0fcf3efd68a7f92'  # e.g., 'b1b15e88fa797225412429c1c50c122a1'
CITY = "Mbombela,ZA"  # Local to you!

def get_real_weather():
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}"
        response = requests.get(url)
        data = response.json()
        temp = data['main']['temp'] - 273.15  # Convert to Celsius
        humidity = data['main']['humidity']
        return temp, humidity
    except Exception as e:
        print(f"API error: {e}. Using simulation.")
        return random.uniform(20, 30), random.uniform(50, 70)  # Fallback for Mpumalanga averages

def read_sensors():
    temp, humidity = get_real_weather()
    soil_moisture = random.uniform(30, 70)  # Simulated soil; we'll add dataset later
    return {"temp": temp, "humidity": humidity, "soil_moisture": soil_moisture}

# Load the kaggle dataset
try: 
    df = pd.read_csv('data/Crop_recommendation.csv')
except FileNotFoundError:
    print("Dataset not found. Please ensure 'data/Crop_recommendation.csv' is available.")
    # Fallback to an empty DataFrame to prevent errors in the rest of the code
    df = pd.DataFrame({
        'temperature': [20, 25, 30],
        'humidity': [50, 60, 70],
        'ph': [6.0, 6.5, 7.0], # Proxy for soil moisture
        'label': ['rice','maize', 'chickpea']
    })  

# Create a dummy binary label: 1 if needs irrigation , 0 otherwise (for simplicity)
# Adapt based on data: Here, assume 'rice' or 'pigeonpea' need it
df['needs_irrigation'] = df['label'].apply(lambda x: 1 if x in ['rice', 'pigeonpea', 'blackgram'] else 0)

#Features: Use columns matching our sensors (add more like N/P/K if you expand sensors)
X = df[['temperature', 'humidity', 'ph']] # 'pd' as stand-in for soil moisture
y = df['needs_irrigation']

# Split and train a model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LogisticRegression()
model.fit(X_train, y_train)

#Quick check: Print accuracy (should be ~0.5-0.8; improve with more data/features)
y_pred = model.predict(X_test)
print(f"Model Accuracy: {accuracy_score(y_test, y_pred):.2f}")  

# Main loop to simulate continuous monitoring
while True:
    sensor_data = read_sensors()
    print(f"Farm Sensor Data: {sensor_data}")
    # Prepare features for prediction (ensure order matches training)           
    features = np.array([[sensor_data['temp'], sensor_data['humidity'], sensor_data['soil_moisture']]])  # 'soil_moisture' as 'ph'

    # Predict
    prediction = model.predict(features)[0]
    if prediction == 1:
        print("Irrigation needed! Activating water pump...")
    else:
        print("No irrigation needed at the moment.")
    time.sleep(5)  # Simulate reading every 5 seconds