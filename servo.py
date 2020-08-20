import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
servo = GPIO.PWM(2, 50)
servo.start(0.0)
 
def setservo(d):
    pulse = 0.5 + 1.9 * (d + 90) / 180
    servo.ChangeDutyCycle(pulse / 20 * 100)

for i in range(5):
        setservo(-90)
	time.sleep(1.0)

        setservo(0)
	time.sleep(1.0)

        setservo(90)
	time.sleep(1.0)

