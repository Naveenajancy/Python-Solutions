def fibonacci_gen():
    trail, lead = 0, 1
    while True:
        yield lead
        trail, lead = lead, trail+lead

fib = fibonacci_gen()
print(fib.__next__())

for _ in range(10):
    print(fib.__next__())

