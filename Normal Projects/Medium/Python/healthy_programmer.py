# Healthy programmer
from pygame import mixer
import time

def music_controller(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break

water_timer  = time.time()
eye_timer = time.time()
exercise_timer = time.time()

water_seconds = 5
eye_seconds = 7
exercise_seconds = 8

while True:
    if time.time() - water_timer > water_seconds:
        print("Write 'drank' to stop the alarm")
        music_controller("water.wav","drank")
        water_timer = time.time()

    if time.time()-eye_timer > eye_seconds:
        print("Write 'done' to stop the alarm")
        music_controller("eye.wav","done")
        eye_timer = time.time()

    if time.time()-exercise_timer > exercise_seconds:
        print("Write 'exdone' to stop the alarm")
        music_controller("exercise.wav","exdone")
        exercise_timer = time.time()