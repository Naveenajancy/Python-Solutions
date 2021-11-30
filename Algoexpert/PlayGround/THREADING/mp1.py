from multiprocessing import Pool
import time

def f(x):
    print(" sleep mode")
    time.sleep(5)
    print("done")
    return x*x

if __name__ == '__main__':
    with Pool(3) as p:
        print(p.map(f, [2, 4, 6]))

