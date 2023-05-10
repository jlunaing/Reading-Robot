'''!    @file       dcmotor_driver.py
        @brief      Motor testing
        @details    This code will need to take in the following values: 
                    time for antenna move and position for servo. May need to 
                    saturate duty cycle.
        @author     Juan Luna
        @date       2021-01-28 Created
'''

import RPi.GPIO as GPIO
from time import sleep



# Pins for Motor Driver Inputs 
DCMotor = 0 #GPIO 0

ServoMotor = 1 #GPIO 1
ServoMotorEN = 2 #GPIO 2
STBYPin = 3 #GPIO 3

def setup():
    GPIO.setmode(GPIO.BCM)              # GPIO Numbering
    GPIO.setup(DCMotor,GPIO.OUT)  # All pins as Outputs
    
    GPIO.setup(ServoMotor,GPIO.OUT)
    GPIO.setup(ServoMotorEN,GPIO.OUT)
    servo_ctr = GPIO.PWM(ServoMotor, 50) #channel = ServoMotor, frequency=50Hz
    
    
    
    GPIO.setup(STBYPin,GPIO.OUT)   #enable motors
    GPIO.output(STBYPin,GPIO.HIGH)
 
def move_antenna():
    # Going forwards
    GPIO.output(DCMotor,GPIO.HIGH)
 
    sleep(5) # will need to remove this for cooperative multitasking
    # stop the motor after t= 5 seconds
    GPIO.output(DCMotor,GPIO.LOW)

def move_arms():
    # Going forwards
    GPIO.output(ServoMotorEN,GPIO.HIGH)
    servo_ctr.start(50) #start pwm signal at 50 duty cycle
    
 
    sleep(1) # will need to remove this for cooperative multitasking
    # stop the motor after some delay
     
    servo_ctr.ChangeDutyCycle (0) # move back to original position
    
    sleep(1) #allow time for movement
    servo_ctr.stop() #start pwm signal at 0 duty cycle
    

def destroy():  
    GPIO.cleanup() #set all ports back to input to protect



if __name__ == '__main__':     # Program start from here
    setup()
    try:
            move_antenna()
            move_arms()
    except KeyboardInterrupt:
        destroy()