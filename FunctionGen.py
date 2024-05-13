import time

def printFunction(width, a, p):
    final_image = ""

    for row in range(width):
        for pixel in range(width):
            x = row - width / 2
            y = pixel - width / 2
            if (x == round(-a * (y ** 2))):
                final_image += "@"
            elif x == 0:
                if y == width/2-1:
                    final_image += ">"
                else:
                    final_image += "-"
            elif y == 0:
                if row == 0:
                    final_image += "^"
                else:
                    final_image += "|"
            else:
                final_image += " "
        final_image += "\n"
    print(final_image + "\n" )
    print("Streckung: " + str(a))


a = 10
while True:
    printFunction(50, a, 2)
    if a < 0.05:
        a = 10
    else:
        a = a / 2
    time.sleep(0.1)
