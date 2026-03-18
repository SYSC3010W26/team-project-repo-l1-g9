import requests, time

DB_URL = "https://lab3-iot-communication-default-rtdb.firebaseio.com"
print("GUI: Manual Override Dashboard")

while True:
    print("\n--- PUMP CONTROL ---")
    choice = input("Enter '1' to turn Pump ON (Blue), '0' to turn Pump OFF (Red), or 'Q' to quit: ")
    
    if choice.upper() == 'Q':
        # Clear the override so auto-mode takes over again
        requests.delete(f"{DB_URL}/commands/override.json")
        print("Exiting manual override. Returning to Auto Mode.")
        break
        
    if choice in ['0', '1']:
        state = True if choice == '1' else False
        payload = {"ts": time.time(), "pump_enable": state, "source": "GUI_User"}
        requests.put(f"{DB_URL}/commands/override.json", json=payload)
        print("Command sent to Firebase!")