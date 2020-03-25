from threading import Thread
from time import sleep
class Hello(Thread):
    def run(self):
        for i in range(5):
            sleep(1)
            print("Hello")

class Hi(Thread):
    def run(self):
        for i in range(5):
            sleep(1)
            print("Hi ")


t1 = Hello()
t2 = Hi()
t1.start()
sleep(0.2)
t2.start()
t1.join()
t2.join()
print("Bye")