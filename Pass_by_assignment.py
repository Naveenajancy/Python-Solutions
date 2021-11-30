#https://realpython.com/python-pass-by-reference/
#Not quite. Python passes arguments neither by reference nor by value, but by assignment.

'''
Python’s built-in id() returns an integer representing the memory address of the desired object. Using id(), you can verify the following assertions:

    Function arguments initially refer to the same address as their original variables.
    Reassigning the argument within the function gives it a new address while the original variable remains unmodified.

In the below example, note that the address of x initially matches that of n but changes after reassignment, while the address of n never changes:
'''


def numbers():
    x = 1000
    print(f" Initial address of x is:{id(x)}")
    new = increment(x)
    print(f" address of x after increment:{id(x)}")
    print(f"New value is {new} and the address is {id(new)}")
def increment(x):
    print(f"The intial address of x is:{id(x)}")
    x += 1
    print(f"The next address of x is:{id(x)} ")
    return x

def compare(x, y):
    a = x
    b = y
    if a is b:
        print(f"The id of a is {id(a)} and the id of b is {id(b)} :TRUE")
   # elif a == b:
    #    print(f"The id of a is {id(a)} and the id of b is {id(b)} :TRUE1")
    else:
        print(f"The id of a is {id(a)} and the id of b is {id(b)} : FALSE")

def replacesting(word):
    r = word.replace('a', 'b')
    print(f"the new word is : {r}")

#numbers()
x = [1]
y = [1]
print(f"id of x : {id(x)} - id of y : {id(y)}")
C = compare(x,y)
print(f"id of x : {id(x)} - id of y : {id(y)}  id of C is : {id(C)}")
replacesting("aallo")

