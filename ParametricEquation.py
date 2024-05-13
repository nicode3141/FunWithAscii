import time
import math
from pysinewave import SineWave

def printFunction(width, r):  # r = radius
    final_image = ""

    for row in range(width):
        for pixel in range(width):
            x = row - width / 2
            y = pixel - width / 2
            t = math.atan2(y, x)
            if x == round(r * math.cos(t)) and y == round(r * math.sin(t)):
                final_image += "@"
            else:
                final_image += "."
        final_image += "\n"
    print(final_image + "\n\n")

sinewave = SineWave(1)
sinewave.play()
a = 50
while True:
    sinewave.set_frequency(a)
    printFunction(50, a)
    if a < 0.05:
        a = 50
        sinewave.set_pitch(100)
    else:
        a = a / 2
    time.sleep(0.1)
