import time
import serial

PORT = "/dev/ttyACM0"
BAUD = 9600

ser = serial.Serial(PORT, BAUD, timeout=1)
time.sleep(2)
print("UART connected:", PORT)

while True:
    line = ser.readline().decode(errors="ignore").strip()
    if line:
        print("Node2 UART:", line)
    time.sleep(0.2)
