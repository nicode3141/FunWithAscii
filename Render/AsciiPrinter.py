import time
import json
import winsound

with open('Dataset.json') as f:
    data = json.load(f)

winsound.PlaySound("../assets/funkytown.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
frames = data.get('frames', [])
while True:
    for frame in frames:
        for key, value in frame.items():
            print(key + ":", value)
            time.sleep(0.07)

