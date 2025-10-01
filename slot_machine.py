import RPi.GPIO as GPIO
import time
import random
from rpi_lcd import LCD

lcd = LCD()

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
light = 17

rigged = False
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
GPIO.setup(light, GPIO.OUT)
GPIO.setup(5, GPIO.IN)
GPIO.setup(27, GPIO.IN)

while True:
    while (GPIO.input(5) == 0):
        
        count = len(chars)
        if rigged == False:
            char1 = random.choice(chars)
            char2 = random.choice(chars)
            char3 = random.choice(chars)
            char4 = random.choice(chars)
        else:
            char1 = random.choice(new_chars)
            char2 = random.choice(new_chars)
            char3 = random.choice(new_chars)
            char4 = random.choice(new_chars)

        lcd.text(char1 + " " + char2 + " " + char3 + " " + char4, 1)
            
        if char1 == char2 == char3 == char4:
            for i in range(100):
                time.sleep(0.05)
                GPIO.output(light, GPIO.HIGH)
                time.sleep(0.05)
                GPIO.output(light, GPIO.LOW)
            GPIO.output(light,GPIO.LOW)
        else:
            time.sleep(0.3)
            GPIO.output(light, GPIO.LOW)
            lcd.clear()
    while(GPIO.input(27) == 0):
        new_chars =  "ABC"
        rigged = True
        print(new_chars)