import time
from pygame import mixer

while True:
    result = time.localtime(time.time())
    print(result.tm_min)
    if result.tm_min == 25:
        mixer.init()
        mixer.music.load("DKBOSE.mp3")
        mixer.music.set_volume(0.7)
        mixer.music.play()
        S = input()
        if S == "drank":
            mixer.music.stop()
    