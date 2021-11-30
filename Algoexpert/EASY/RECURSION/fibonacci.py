'''
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

terms = 100
for i in range(terms):
    print(f"Fibonacci of {i} {fibonacci(i)}")
'''

def getNthFib(n):
    # Write your code here.
    fibocache = {}
    if type(n) != int:
        raise TypeError("n must be positive integer")
    if n < 0:
        raise TypeError("n must be postive integer")
    if n == 1:
        value = 0
    elif n == 2:
        value=1
    elif n>2:
        value = getNthFib(n-1) + getNthFib(n-2)
    fibocache[n] = value
    print (f" i {n}  {fibocache}")
    return fibocache[n]


e = 6
print(f"fibo of {e} {getNthFib(e)}")