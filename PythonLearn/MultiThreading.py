from threading import *
from time import sleep

class Morning(Thread):
    def run(self):
        for i in range(5):
            print("Good Morning")
            sleep(1)


class Evening(Thread):
    def run(self):
        for i in range(5):
            print("Good Evening")
            sleep(1)


t1= Morning()
t2=Evening()
t1.start()
t2.start()

t1.join()
t2.join()

print("Bye")