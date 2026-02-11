import random
import time
import requests
import json

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

# Main loop to simulate continuous monitoring
while True:
    sensor_data = read_sensors()
    print(f"Farm Sensor Data: {sensor_data}")
    time.sleep(5)  # Simulate reading every 5 seconds