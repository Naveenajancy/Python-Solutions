"""
The join() method basically is used to join the input string by another set of separator/string elements.
It accepts iterables such as set, list, tuple, string, etc and another string(separable element) as par
"""

def joinfun():
    s = input("please enter your string\n")
    return '*'.join((str(x)) for x in s)


output = joinfun()
print(f"output {output}")