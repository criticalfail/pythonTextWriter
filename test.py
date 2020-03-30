from random import random
import time
with open("test.txt","r") as f:
    while True:
        c=f.read(1)
        print(c)
        time.sleep(random()*0.5)