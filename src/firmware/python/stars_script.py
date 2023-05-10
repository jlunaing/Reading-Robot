'''!    @file   stars_script.py
        @brief  "Unicorn Hat" LED Screen test script
        @author Juan Luna
        @date   2021-05-26 Created
'''

import random
import time
import unicornhathd

unicornhathd.brightness(0.6)

star_count = 25
star_speed = 0.05
stars = []

t0 = time.time()
curr_time = 0
for i in range(0, star_count):
    stars.append((random.uniform(4, 11), random.uniform(4, 11), 0))

try:
    while curr_time < 3:
        unicornhathd.clear()

        for i in range(0, star_count):
            stars[i] = (
                stars[i][0] + ((stars[i][0] - 8.1) * star_speed),
                stars[i][1] + ((stars[i][1] - 8.1) * star_speed),
                stars[i][2] + star_speed * 50)

            if stars[i][0] < 0 or stars[i][1] < 0 or stars[i][0] > 16 or stars[i][1] > 16:
                stars[i] = (random.uniform(4, 11), random.uniform(4, 11), 0)

            v = stars[i][2]

            unicornhathd.set_pixel(stars[i][0], stars[i][1], v, v, v)

        unicornhathd.show()
        curr_time = time.time() - t0
    unicornhathd.off()
except KeyboardInterrupt:
    unicornhathd.off()