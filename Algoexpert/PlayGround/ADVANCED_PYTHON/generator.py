import random

def lottery():
    for i in range(3):
        yield random.randint(10, 20)
    yield random.randint(1,5)

# for ran_num in lottery():
#     print(f"Random number is  {ran_num}")

def y ():
    for i in range(10):
        yield i

ins = y()
print(ins)
print(next(ins))
print(next(ins))
print(next(ins))