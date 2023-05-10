'''!    @file   LEDneutral_script.py
        @brief  Different faces for the robot using LED screen
        @author Juan Luna
        @date   2021-05-26 Created
'''

import unicornhathd as unicorn
import colorsys
import RPi.GPIO as GPIO

# faces

happy =        [ [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0],
                  [0,0,0,1,1,1,0,0,0,0,1,1,1,0,0,0],
                  [0,0,0,1,1,1,0,0,0,0,1,1,1,0,0,0],
                  [0,0,0,1,0,1,0,0,0,0,1,0,1,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0],
                  [0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0],
                  [0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

smile =       [ [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,1,1,1,0,0,0,0,1,1,1,0,0,0],
                  [0,0,0,1,0,1,0,0,0,0,1,0,1,0,0,0],
                  [0,0,0,1,1,1,0,0,0,0,1,1,1,0,0,0],
                  [0,0,0,1,1,1,0,0,0,0,1,1,1,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0],
                  [0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0],
                  [0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

neutral =       [ [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,1,1,1,0,0,0,0,1,1,1,0,0,0],
                  [0,0,0,1,1,1,0,0,0,0,1,1,1,0,0,0],
                  [0,0,0,1,1,1,0,0,0,0,1,1,1,0,0,0],
                  [0,0,0,1,0,1,0,0,0,0,1,0,1,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0],
                  [0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]


# variable for setting color
h = 0.0


# set color function
def set_color(color):
  global h
    
  if color == "red":
      h = 0.0
  elif color == "orange":
      h = 0.08
  elif color == "yellow":
      h = 0.16
  elif color == "green":
      h = 0.33
  elif color == "blue":
      h = 0.67
  elif color == "purple":
      h = 0.75
  else:
      h = 0.0

# set/display pixels
def set_pixels(color, face):
    global h
    unicorn.brightness(1.0)
    unicorn.off()
    for x in range(16):
        for y in range(16):
            set_color(color)
            s = 1.0
            v = face [x] [y]
            r,g,b = colorsys.hsv_to_rgb(h, s, v)
            red = int(r*255.0)
            green = int(g*255.0)
            blue = int(b*255.0)
            unicorn.set_pixel(x, y, red, green, blue)
        unicorn.show()
        unicorn.rotation(180)

try:        
    set_pixels("orange", neutral)
        
finally:
    GPIO.cleanup()