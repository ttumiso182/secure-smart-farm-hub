# Secure Smart Farm Hub

An open-source, zero-cost Python project simulating a secure IoT system for rural farm monitoring in Mpumalanga, South Africa. It fetches real-time weather data, uses AI to predict irrigation needs, and adds cybersecurity with encryption and simulated transmission. Built for BICT honours exploration in AI, IoT, and cybersecurity—fully simulated for broke-student mode, but scalable to real hardware.

## Overview
This project started as a way to restart GitHub projects post-BICT degree. It's a single Python script (`src/main.py`) that:
- Simulates IoT sensors using free APIs and random data.
- Applies AI (machine learning) for smart predictions.
- Secures data with encryption and anomaly checks before "sending" via MQTT.

Relevant to Mpumalanga agriculture (e.g., macadamia or citrus farms) for monitoring soil, temp, and humidity to optimize irrigation and detect issues.

## Features
- **IoT Simulation**: Pulls live Mbombela weather from OpenWeatherMap API; simulates soil moisture.
- **AI Predictions**: Trains a Logistic Regression model on a free Kaggle dataset to predict if irrigation is needed (e.g., accuracy ~0.91).
- **Cybersecurity**: Encrypts data with Fernet, detects anomalies (e.g., impossible temps), and sends via free MQTT broker.
- **Free & Local**: No hardware required; runs on your PC with Anaconda/Python.
- **Infinite Loop**: Mimics real-time monitoring; stop with Ctrl+C.

## Tech Stack
- Python 3 (via Anaconda)
- Libraries: `requests` (API), `pandas` & `scikit-learn` (AI), `cryptography` (encryption), `paho-mqtt` (transmission)
- Data: OpenWeatherMap API (free key), Kaggle "Crop_recommendation.csv" (free download)
- Tools: VS Code, GitHub

## Setup
1. **Clone the Repo**: In VS Code, Git: Clone > https://github.com/ttumiso182/secure-smart-farm-hub.git
2. **Virtual Environment** (using Anaconda for your setup):
   - Open terminal in VS Code: `conda activate base` (or create a new one: `conda create -n farm-hub python=3.10 && conda activate farm-hub`)
3. **Install Dependencies**:
pip install numpy scikit-learn cryptography paho-mqtt pandas requests
4. **API Key**: Sign up at openweathermap.org (free). Paste your key into `src/main.py` at `API_KEY = "your_key_here"`.
5. **Dataset**: Download "Crop_recommendation.csv" from Kaggle[](https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset). Place in `/data/` folder.

## How to Run
1. In VS Code terminal: Navigate to repo root, activate env if needed.
2. Run: `python src/main.py`
3. Output: Model trains, then loops every 5s with sensor data, AI prediction, encryption, and "send" confirmation.
- Example:

      Model Accuracy: 0.91
      Encryption Key generated: sWihMQVTpAvG3lgglx5IGqvrtx5u5O_OozUT1auYnP4=
      Farm Sensor Data: {'temp': 28.160000000000025, 'humidity': 61, 'soil_moisture': 64.76593144532957}
      Irrigation needed! Activating water pump...
      Encrypted data: b'gAAAAABpjusp1mL6byQ66OXqt6bQ9FE99dwXSyHAD3mXCcmIWm'...
      Secure encrypted data sent to broker!

4. Stop: Ctrl+C (adds graceful exit if you implemented the try/except).
5. Test MQTT: Use free MQTT Explorer app to subscribe to "smart_farm_hub/secure_data" on broker.emqx.io—see encrypted payloads.

## Code Structure
- **Imports**: All libraries at top.
- **Constants**: API_KEY, CITY (Mbombela,ZA).
- **Functions**:
- `get_real_weather()`: Fetches API data or simulates fallback.
- `read_sensors()`: Combines weather with simulated soil.
- **AI Training**: Loads Kaggle CSV, creates binary label (needs_irrigation), trains LogisticRegression.
- **Main Loop**: Reads sensors, predicts, encrypts, checks anomalies, sends via MQTT.
- **Error Handling**: Try/except for API/MQTT; warnings suppressed if added.

Full code in `src/main.py`. Warnings (e.g., sklearn feature names) are harmless—fixed by using pd.DataFrame for predictions.

## Scalability Ideas
To make this bigger (e.g., for honours research or real deployment):
1. **Add Real Hardware**: Replace simulations with Raspberry Pi/ESP32 + sensors (DHT11 for temp/humidity, capacitive soil sensor). Use libraries like `adafruit_dht`. Budget: ~R500 from Takealot.
2. **Enhance AI**: 
- Use more features (e.g., add rainfall from API).
- Switch to advanced models (e.g., RandomForestClassifier for better accuracy).
- Fine-tune on local Mpumalanga data (e.g., from SA Weather Service APIs).
- Add crop recommendations: Predict full 'label' from dataset instead of binary.
3. **Improve Cybersecurity**:
- Store keys securely (e.g., in .env file with python-dotenv).
- Add authentication to MQTT (use private broker like Mosquitto on a VPS).
- Implement full IDS: Use ML to detect patterns in logs.
4. **Deployment**:
- Run on a server: Use Flask/Django for a web dashboard (view data/predictions online).
- Cloud: Deploy to free tiers (Heroku, Vercel) or AWS Free Tier for real-time hosting.
- Mobile App: Integrate with MIT App Inventor for alerts via push notifications.
5. **Data Logging**: Save readings to CSV/SQLite for historical analysis (add `pd.to_csv` in loop).
6. **Testing**: Add unit tests with pytest (e.g., test model accuracy >0.8).
7. **Interdisciplinary**: Collaborate—link to space data (e.g., NASA APIs for satellite soil moisture) tying back to AI in space comms.

Start small: Fork the repo for experiments, use branches (e.g., `git checkout -b add-hardware`).

## License
MIT License—feel free to modify and share.

## Troubleshooting
- sklearn Warning: Fixed by using pd.DataFrame for predictions.

## Next Steps / Contributions
- Issues: Report bugs on GitHub.
- Pull Requests: Add features like visualizations (matplotlib plots).
- Questions: Ping me on LinkedIn or here.

Built by Tumiso in Mbombela, Mpumalanga. Last updated: February 2026.

