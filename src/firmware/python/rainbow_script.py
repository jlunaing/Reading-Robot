'''!    @file   rainbow_script.py
        @brief  Demo showing LED screen capabilities
        @author Juan Luna
        @date   2021-05-26 Created
'''

import colorsys
import math
import time

import unicornhathd

unicornhathd.rotation(0)
unicornhathd.brightness(0.6)

step = 0

try:
    while step <180:
        step += 1
        for x in range(0, 16):
            for y in range(0, 16):
                dx = 7
                dy = 7

                dx = (math.sin(step / 20.0) * 15.0) + 7.0
                dy = (math.cos(step / 15.0) * 15.0) + 7.0
                sc = (math.cos(step / 10.0) * 10.0) + 16.0

                h = math.sqrt(math.pow(x - dx, 2) + math.pow(y - dy, 2)) / sc

                r, g, b = colorsys.hsv_to_rgb(h, 1, 1)

                r *= 255.0
                g *= 255.0
                b *= 255.0

                unicornhathd.set_pixel(x, y, r, g, b)

        unicornhathd.show()
        time.sleep(1.0 / 60)
    unicornhathd.off()
    
except KeyboardInterrupt:
    unicornhathd.off()