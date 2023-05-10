'''!    @file   register.py
        @brief  Serial port service registering script
        @author Juan Luna
        @date   2021-05-26 Created
'''

import subprocess
import RPi.GPIO as GPIO
import time

from subprocess import call

rc = call("sudo ./bluetooth_adv", shell=True)

call("python servoMID_script.py && python motor1.5_script.py", shell = True)

exec(open("LEDsmile_script.py").read())

