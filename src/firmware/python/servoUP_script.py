'''!    @file       servoUP_script.py
        @brief      Servo motor testing
        @details    This code will need to take in the following values: 
                    time for antenna move and position for servo. May need to 
                    saturate duty cycle.
        @author     Juan Luna
        @date       2021-01-28 Created
'''

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
  
Servo_PWR =2  # BCM pin 2
Servo_PWM = 27  # BCM pin 27
STBYPin = 3  # Bcm pin 2

 # GPIO Numbering
GPIO.setup(Servo_PWR,GPIO.OUT) 
GPIO.setup(Servo_PWM,GPIO.OUT)
# GPIO.setup(STBYPin, GPIO.OUT)

# GPIO.output(STBYPin,GPIO.LOW)

servo_ctr = GPIO.PWM(Servo_PWM, 50) #channel = ServoMotor, frequency=50Hz 


GPIO.output(Servo_PWR,GPIO.HIGH)
servo_ctr.start(8) #PWM for servo up position
sleep(3) # stop the motor after some delay
servo_ctr.stop() #start pwm signal at 0 duty cycle
GPIO.output(Servo_PWR, GPIO.LOW)

