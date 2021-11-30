from threading import *
import time
l = Lock()
def userdetails(name, age):
    for i in range(3):
        l.acquire()
        print("lock is acquired")
        print(f"Hi {name} ")
        time.sleep(3)
        print(f"Your age is: {age}")
        l.release()
        print("Lock is released")

t1 = Thread(target=userdetails, args=("Naveena", 30))
t2 = Thread(target=userdetails, args=("Sam", 20))

t1.start()
t2.start()