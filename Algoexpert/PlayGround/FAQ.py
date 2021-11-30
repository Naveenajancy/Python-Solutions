class Person:
    def __call__(self):
        print("hello")


p = Person()
print(callable(type(p)))
p()
print(p)
