import time
from sense_hat import SenseHat

print("--- HW-TEST 1: SENSE-HAT CLIMATE SENSORS ---")
print("Isolating I2C temperature and humidity readings...")
sense = SenseHat()

for i in range(5):
    temp = sense.get_temperature()
    hum = sense.get_humidity()
    print(f"Reading {i+1}/5 -> Temp: {round(temp, 2)}C | Humidity: {round(hum, 2)}%")
    
    # Automated assertions
    assert 0 < temp < 50, f"Hardware Error: Temp {temp} is out of realistic bounds!"
    assert 0 <= hum <= 100, f"Hardware Error: Humidity {hum} is out of bounds!"
    time.sleep(1)

print("RESULT: PASS. Hardware sensors are functional and returning valid floats.")