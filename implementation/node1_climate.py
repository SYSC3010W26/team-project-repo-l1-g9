import time
import requests
import RPi . GPIO as GPIO
from smbus2 import SMBus


# --- Configuration ---
FIREBASE_URL = "https://lab3-iot-communication-default-rtdb.firebaseio.com"
FAN_PIN = 17
TEMP_THRESHOLD = 27.0

# --- Hardware Setup ---
GPIO.setmode (GPIO.BCM)
GPIO.setup (FAN_PIN, GPIO.OUT)

# AHT20 I2C Setup
bus = SMBus (1)
AHT20_ADDR = 0x38

def read_aht20 () :
    """ Reads raw bytes from AHT20 via I2C and converts to C and %RH."""
    try:
        # Trigger measurement
        bus . write_i2c_block_data ( AHT20_ADDR , 0xAC ,[0x33 , 0x00 ])
        time . sleep (0.1)
        # Read 6 bytes of data
        data = bus . read_i2c_block_data ( AHT20_ADDR , 0x00 , 6)

        # Bitwise conversion as per datasheet
        temp_c = (( data [3] & 0x0F ) << 16 | data [4] << 8 | data [5]) * 200.0 / 1048576.0 - 50
        hum_pct = (( data [1] << 12) | ( data [2] << 4) | ( data [3] >> 4) ) * 100.0 / 1048576.0
        return round ( temp_c , 2) , round ( hum_pct , 2)
    except Exception as e:
        print ( f"I2C Read Error : {e}")
        return None , None

def control_fan (current_temp) :
    """ FR1 : Toggles fan based on threshold."""
    if current_temp > TEMP_THRESHOLD:
        GPIO.output (FAN_PIN, GPIO.LOW) # Transistor ON -> Relay Closed
        return True
    else:
        GPIO.output (FAN_PIN, GPIO.HIGH) # Transistor OFF -> Relay Open
        return False

# --- Main Control Loop ---
if __name__ == '__main__':
    print (" Node 1: Climate Monitor Started.")
    try:
        while True:
            temp, hum = read_aht20 ()

            if temp is not None:
                # 1. Evaluate safety threshold & Actuate Fan
                fan_status = control_fan ( temp )
                print ( f" Temp : {temp}C | Hum:{hum}% | Fan ON: {fan_status}")

                # 2. Construct Payload (matching Design Doc data format)
                payload = {
                "ts": int (time.time()) ,
                "temperature_c": temp ,
                "humidity_pct": hum ,
                "source": "node1"
                }

                # 3. Publish to Cloud (FR3 )
                try:
                    # Firebase uses POST to append objects with unique <push_id >
                    resp = requests . post (f"{ FIREBASE_URL }/nodes/node1/climate.json", json = payload)
                    if resp.status_code == 200:
                        print ("Data published to Firebase successfully.")
                except requests . exceptions . RequestException as e :
                    print ( f" Network Error : {e}")

            # FR3 : Fixed interval of 60 seconds
            time.sleep (60)

    except KeyboardInterrupt:
        print ("\nShutting down Node 1...")
    finally:
        # ALWAYS clean up GPIO safely to prevent relay from staying stuck ON
        GPIO.cleanup()
        print ("GPIO Cleaned. Exiting.")

