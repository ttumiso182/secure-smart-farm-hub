## Setup Instructions
1. Clone the repo.
2. Create venv: `python -m venv venv`
3. Activate: `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (other)
4. Install: `pip install -r requirements.txt` (we'll add this file next)

## Cybersecurity Features
- Data encryption with Fernet (symmetric key).
- Anomaly detection for tampered readings.
- Secure transmission simulation via public MQTT broker.

Run the full demo: `python src/main.py`
