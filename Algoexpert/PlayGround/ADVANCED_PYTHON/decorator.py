def my_decorator(func):
    def wper(*args, **kwargs):
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wper

@my_decorator
def say_whee():
    print("Whee!")

def do_twice(func):
    def wrapperDoTwice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapperDoTwice

@do_twice
def hello(name):
    print(f"Hello  {name} !!")

#say_whee = my_decorator(say_whee)
#print(say_whee)
print(say_whee())

hello("jesus")