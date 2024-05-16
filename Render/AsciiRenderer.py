import cv2 as cv
import time
import json

# OpenCV library



frames_out = []

def print_image(image_src):
    image = cv.VideoCapture(image_src)
    frames = []
    ret, frame = image.read()

    while ret:
        frame_count = 0
        ret, frame = image.read()
        if not ret:
            break
        aspect_ratio = frame.shape[1] / float(frame.shape[0])
        new_height = int(100 / aspect_ratio / 2)
        resized_image = cv.resize(frame, (100, new_height))

        ascii_chars = "@%#*+=-:. "
        ascii_chars_inverted = " .:=+*#%@"

        ascii_image = ""
        for row in resized_image:
            for pixel in row:
                intensity = int(pixel.mean() / 255 * (len(ascii_chars) - 1)) # get median of RGB values and divide by 255
                ascii_image += ascii_chars_inverted[intensity]
            ascii_image += "\n"

        frames_out.append(ascii_image)
        frame_count+= 1
        print(ascii_image)
        time.sleep(0.07)
    generateJSON(frames_out)

def generateJSON(frames_out):
    frames_json = {"frames": []}
    for idx, frame in enumerate(frames_out, start=1):
        frames_json["frames"].append({f"frame_{idx}": frame})
    with open("Dataset.json", "w") as f:
        f.write(json.dumps(frames_json))



print_image("../assets/chip.gif")


#asciiChip = image_to_ascii(r"C:\Users\nicol\PycharmProjects\FunWithAscii\assets\chip.gif")

#image_to_print = print_image("assets/Sonne.png")

#print(image_to_print)