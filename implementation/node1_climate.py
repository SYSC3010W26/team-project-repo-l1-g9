import time, requests
from sense_hat import SenseHat

DB_URL = "https://lab3-iot-communication-default-rtdb.firebaseio.com" 
sense = SenseHat()

print("Node 1: Climate Monitor Started...")

while True:
    temp = round(sense.get_temperature(), 2)
    hum = round(sense.get_humidity(), 2)
    
    payload = {"ts": time.time(), "temperature_c": temp, "humidity_pct": hum, "source": "node1"}
    
    try:
        r = requests.post(f"{DB_URL}/nodes/node1/climate.json", json=payload)
        print(f"Published to Firebase -> Temp: {temp}C, Humidity: {hum}%")
    except Exception as e:
        print("Network error connecting to Firebase.")
        
    time.sleep(5)