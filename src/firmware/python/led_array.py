'''!    @file   led_array.py
        @brief  Different faces for the robot using LED screen
        @author Juan Luna
        @date   2021-05-26 Created
'''

import unicornhathd as unicorn
import time
import colorsys
import numpy
import RPi.GPIO as GPIO

GPIO.setup(LED,GPIO.OUT)  # initialize GPIO-21 (LED) as an output Pin
GPIO.output(LED,0)

server_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

port = 1
server_socket.bind(("",port))
server_socket.listen(1)

client_socket,address = server_socket.accept()
print ("Accepted connection from ",address)
while 1:

    data = client_socket.recv(1024)
    print ("Received: %s" % data)

    if (data == "0"):    # if '0' is sent from the Android App, turn OFF the LED
        print ("HAPPY FACE")
        set_pixels(face_happy)

    if (data == "1"):    # if '1' is sent from the Android App, turn OFF the LED
        print ("SAD FACE")
        set_pixels(face_down)

    if (data == "q"):
        print ("Quit")
        break

client_socket.close()
server_socket.close()

# eyes------------import RPi.GPIO as GPIO--------------------------

eyes_happy = [[0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0],
              [0,0,0,1,1,1,0,0,0,0,1,1,1,0,0,0],
              [0,0,0,1,1,1,0,0,0,0,1,1,1,0,0,0],
              [0,0,0,1,0,1,0,0,0,0,1,0,1,0,0,0]]

eyes_center = [[0,0,0,1,1,1,0,0,0,0,1,1,1,0,0,0],
               [0,0,0,1,0,1,0,0,0,0,1,0,1,0,0,0],
               [0,0,0,1,1,1,0,0,0,0,1,1,1,0,0,0],
               [0,0,0,1,1,1,0,0,0,0,1,1,1,0,0,0]]

eyes_down = [[0,0,0,1,1,1,0,0,0,0,1,1,1,0,0,0],
             [0,0,0,1,1,1,0,0,0,0,1,1,1,0,0,0],
             [0,0,0,1,1,1,0,0,0,0,1,1,1,0,0,0],
             [0,0,0,1,0,1,0,0,0,0,1,0,1,0,0,0]]

eyes_left = [[0,0,0,1,1,1,0,0,0,0,1,1,1,0,0,0],
             [0,0,0,0,1,1,0,0,0,0,0,1,1,0,0,0],
             [0,0,0,1,1,1,0,0,0,0,1,1,1,0,0,0],
             [0,0,0,1,1,1,0,0,0,0,1,1,1,0,0,0]]

eyes_right = [[0,0,0,1,1,1,0,0,0,0,1,1,1,0,0,0],
              [0,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0],
              [0,0,0,1,1,1,0,0,0,0,1,1,1,0,0,0],
              [0,0,0,1,1,1,0,0,0,0,1,1,1,0,0,0]]

eyes_up = [[0,0,0,1,0,1,0,0,0,0,1,0,1,0,0,0],
           [0,0,0,1,1,1,0,0,0,0,1,1,1,0,0,0],
           [0,0,0,1,1,1,0,0,0,0,1,1,1,0,0,0],
           [0,0,0,1,1,1,0,0,0,0,1,1,1,0,0,0]]

eyes_big = [[0,0,0,1,1,1,0,0,0,0,1,1,1,0,0,0],
            [0,0,0,1,1,1,0,0,0,0,1,1,1,0,0,0],
            [0,0,0,1,1,1,0,0,0,0,1,1,1,0,0,0],
            [0,0,0,1,1,1,0,0,0,0,1,1,1,0,0,0]]

eyes_creepy = [[0,0,0,1,1,1,0,0,0,0,1,1,1,0,0,0],
               [0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0],
               [0,0,0,1,1,1,0,0,0,0,1,1,1,0,0,0],
               [0,0,0,1,1,1,0,0,0,0,1,1,1,0,0,0]]

# mouths

mouth_smile1 = [[0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0],
                [0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0],
                [0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0]]

mouth_smile2 = [[0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0],
                [0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0],
                [0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0]]

mouth_center = [[0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0],
                [0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0]]

mouth_left = [[0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0],
              [0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0]]

mouth_right = [[0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0],
               [0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0]]

mouth_straight = [[0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0],
                  [0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0]]

# noses

nose_beak = [[0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0]]

nose_center = [[0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0],
               [0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0]]

nose_down = [[0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0],
             [0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0]]

nose_left = [[0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0]]

nose_right = [[0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0]]

nose_small = [[0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0]]


blank = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

# faces

# happy face no nose
face_happy = 2 * blank + eyes_happy + 4 * blank + mouth_smile1 + 3 * blank
face_happy = numpy.array(face_happy)

# happy face with center nose
face_happy_nose1 = 2 * blank + eyes_happy + blank + nose_center + blank + mouth_smile2 + blank
face_happy_nose1 = numpy.array(face_happy_nose1)

# happy face with small nose
face_happy_nose2 = 2 * blank + eyes_happy + 2 * blank + nose_small + 2 * blank + mouth_smile2 + blank
face_happy_nose2 = numpy.array(face_happy_nose2)

# face looking up no nose
face_up = 2 * blank + eyes_up + 7 * blank + mouth_center + blank
face_up = numpy.array(face_up)

# face looking right no nose
face_right = 2 * blank + eyes_right + 7 * blank + mouth_right + blank
face_right = numpy.array(face_right)

# face looking right with nose
face_right_nose = 2 * blank + eyes_right + blank + nose_right + 2 * blank + mouth_right + blank
face_right_nose = numpy.array(face_right_nose)

# face looking left no nose
face_left = 2 * blank + eyes_left + 7 * blank + mouth_left + blank
face_left = numpy.array(face_left)

# face looking right with nose
face_left_nose = 2 * blank + eyes_left + blank + nose_left + 2 * blank + mouth_left + blank
face_left_nose = numpy.array(face_left_nose)

# face looking down no nose
face_down = 2 * blank + eyes_down + 7 * blank + mouth_straight + blank
face_down = numpy.array(face_down)

# face looking down with nose
face_down_nose = 2 * blank + eyes_down + 2 * blank + nose_down + 2 * blank + mouth_straight + blank
face_down_nose = numpy.array(face_down_nose)

# face looking down with smile
face_down_smile = 2 * blank + eyes_down + 4 * blank + mouth_smile1 + 3 * blank
face_down_smile = numpy.array(face_down_smile)

def set_pixels(face):
    unicorn.brightness(1.0)
    unicorn.off()
    for x in range(16):
        for y in range(16):
            h = 1.0
            s = 1.0
            v = face[x,y]
            r,g,b = colorsys.hsv_to_rgb(h, s, v)
            red = int(r*100.0)
            green = int(g*100)
            blue = int(b*100)
            unicorn.set_pixel(x, y, red, green, blue)
        unicorn.show()
        
try:        
    while True:
        set_pixels(face_happy)
        time.sleep (5)
        set_pixels(face_left)
        time.sleep (5)
        set_pixels(face_right)
        time.sleep (5)
        set_pixels(face_up)
        time.sleep (5)
        set_pixels(face_down)
        time.sleep (5)
        
finally:
    GPIO.cleanup()