'''!    @file   motor3_script.py
        @brief  DC motor testing (antenna)
        @author Juan Luna
        @date   2021-05-26 Created
'''

import RPi.GPIO as GPIO
from time import sleep

DC_Pin = 0  # Physical pin 27
STBYPin = 3 # Physical pin 5

def setup():
    global DC_Pin
    global STBYPin
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(DC_Pin,GPIO.OUT)
    GPIO.setup(STBYPin,GPIO.OUT) 
    GPIO.setup(STBYPin,GPIO.OUT)
    GPIO.output(STBYPin,GPIO.HIGH)
    
def move_antenna():
    global DC_Pin
    
    GPIO.output(DC_Pin,GPIO.HIGH)
    sleep(3)
    GPIO.output(DC_Pin,GPIO.LOW)

def destroy():  
    GPIO.cleanup()
        
if __name__ == '__main__': 
    setup()
    
    try:
        move_antenna()
        destroy()
        
    except KeyboardInterrupt:
        destroy()