from random import random
import time
from pynput.keyboard import Controller

keyboard=Controller()
time.sleep(5)
with open("test.txt","r") as f:
    while True:
        c=f.read(1)
        keyboard.type(c)
        time.sleep(random()*0.5)