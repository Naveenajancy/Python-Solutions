"""Have the function FirstFactorial(num) take the num parameter being passed and return the factorial of it.
 For example: if num = 4, then your program should return (4 * 3 * 2 * 1) = 24.
  For the test cases, the range will be between 1 and 18 and the input will always be an integer.
"""
import math

def mathfact(num):
    return math.factorial(num)
def Factorial(num):
  # code goes here

    temp = 1
    for i in range(1, num):
        temp *= num
        num = num-1
        #print(f"i : {i} num: {num} temp : {temp}\n", end="")
    return temp

def FirstFactorial(num):

    # code goes here
    if num==1:
      return 1
    else:
      return (num*FirstFactorial(num-1))
    return num


a = Factorial(4)
print("My amswer", a)
print(mathfact(5))
#b = FirstFactorial(4)
#print("final answer", b)
