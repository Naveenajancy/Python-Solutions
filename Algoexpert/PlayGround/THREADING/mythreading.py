import time
import threading
import concurrent.futures

''' 1. Bottleneck this program executes step by step'''
# print(1)
# time.sleep(10)
# print("done sleeping")
# print(2)
# print("done")

def sleep_time(sec):
    ''' 2. Have to start each thread manually'''
    print("Good night \n")
    time.sleep(sec)
    print("Woke up")

x1 = threading.Thread(target=sleep_time, args=(1,))
x2 = threading.Thread(target=sleep_time, args=(5,))


# x1.start()
# x2.start()
# print(f"Active thread : {threading.activeCount()}")
# time.sleep(1.2)
# print('Done')

start = time.perf_counter()
print(f" start time {start}")

def do_something(seconds):
    print(f'Sleeping {seconds} seconds ...')
    time.sleep(seconds)
    print(f'Done Sleeping {seconds}')

with concurrent.futures.ThreadPoolExecutor() as e:
    #secs = [1, 2, 3, 4, 5]
    secs = [5, 4, 3, 2, 1]
    results = e.map(do_something, secs)

finish = time.perf_counter()
print(f"end time {finish}")
print(f"Finished in {round(finish-start, 2)} seconds")