import os, time

print("Node 3: Health Camera Started...")
while True:
    print("Taking diagnostic picture of greenhouse...")
    os.system("rpicam-jpeg -o plant_health_latest.jpg -t 2000")
    print("Picture saved as plant_health_latest.jpg")
    time.sleep(15)