import time

#for i in reversed(range(10)):
#    print(i)
#    time.sleep(1)

def range_negative_number(array):
    n = len(array)
    print(f"Length of array {n}")

    for i in range(n-1, 0 , -1):
        print(i)

range_negative_number([10,20,34,5,6,8,9,2,3])