'''!    @file   test.py
        @brief  RPi GPIO test
        @author Juan Luna
        @date   2021-05-26 Created
'''
import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)

DC_Pin = 0  # Physical pin 27
STBYPin = 3 # Physical pin 5

          # GPIO Numbering
GPIO.setup(DC_Pin,GPIO.OUT)  # Set up pins as outputs
GPIO.setup(STBYPin,GPIO.OUT) 
GPIO.setup(STBYPin,GPIO.OUT)   # Enable motors
GPIO.output(STBYPin,GPIO.HIGH)
    
GPIO.output(DC_Pin,GPIO.HIGH)
sleep(5)                       # 5-second run time
GPIO.output(DC_Pin,GPIO.LOW)

GPIO.cleanup() # Set all ports back to input to protect
        
        
        
