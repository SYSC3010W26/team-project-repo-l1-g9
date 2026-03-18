import time, requests, random
from sense_hat import SenseHat

DB_URL = "https://lab3-iot-communication-default-rtdb.firebaseio.com"
sense = SenseHat()

blue = (0, 0, 255) # Color for Pump ON (Water)
red = (255, 0, 0)  # Color for Pump OFF (Dry)

def set_pump(state):
    if state:
        sense.clear(blue)
        print("ACTUATOR TRIGGERED: PUMP IS ON (BLUE)")
    else:
        sense.clear(red)
        print("ACTUATOR TRIGGERED: PUMP IS OFF (RED)")

print("Node 2: Irrigation Manager Started...")

while True:
    fake_moisture = random.randint(10, 60) # Simulating soil moisture
    
    try:
        # Check Firebase for manual override
        cmd_req = requests.get(f"{DB_URL}/commands/override.json").json()
        
        if cmd_req and "pump_enable" in cmd_req:
            print("MANUAL OVERRIDE ACTIVE from GUI")
            set_pump(cmd_req["pump_enable"])
        else:
            # Automatic Logic based on fake moisture
            print(f"AUTO MODE -> Current Soil Moisture: {fake_moisture}%")
            if fake_moisture < 30: # If soil is dry, turn pump ON
                set_pump(True)
            else:
                set_pump(False)
    except Exception as e:
        print("Waiting for Firebase connection...")
        
    time.sleep(3)