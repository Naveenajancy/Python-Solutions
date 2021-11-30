from threading import *
import time
l=RLock()
def factorial(n):
   l.acquire()
   print("lock acquired")
   if n==0:
       result=1
   else:
       result=n*factorial(n-1)
   l.release()
   print("Lock is released")
   return result

def results(n):
   print("The Factorial of", n, "is:", factorial(n))

t1=Thread(target=results, args=(4,))
t2=Thread(target=results, args=(6,))

t1.start()
t2.start()