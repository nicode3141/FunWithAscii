import cv2 as cv
import time
# OpenCV library

def image_to_ascii(image_src):
    image_greyscale = cv.imread()

    aspect_ratio = image_greyscale.shape[1] / float(image_greyscale.shape[0])
    new_height = int(100 / aspect_ratio / 2)
    resized_image = cv.resize(image_greyscale, (100, new_height))

    ascii_chars = "@%#*+=-:. "

    ascii_image = ""
    for row in resized_image:
        for pixel in row:
            ascii_image += ascii_chars[pixel // 32]
        ascii_image += "\n"

    return ascii_image

def print_image(image_src):
    image = cv.VideoCapture(image_src)
    frames = []
    ret, frame = image.read()

    while ret:
        ret, frame = image.read()
        if not ret:
            break
        aspect_ratio = frame.shape[1] / float(frame.shape[0])
        new_height = int(100 / aspect_ratio / 2)
        resized_image = cv.resize(frame, (100, new_height))

        ascii_chars = "@%#*+=-:. "

        ascii_image = ""
        for row in resized_image:
            for pixel in row:
                ascii_image += ascii_chars[pixel / 32]
            ascii_image += "\n"

        return ascii_image



image = print_image("assets/chip.gif")
print(image)

#asciiChip = image_to_ascii(r"C:\Users\nicol\PycharmProjects\FunWithAscii\assets\chip.gif")

#image_to_print = print_image("assets/Sonne.png")

#print(image_to_print)