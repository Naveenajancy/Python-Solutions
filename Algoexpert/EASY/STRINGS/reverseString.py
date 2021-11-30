def reverseString(string):

    if len(string) == 0:
        return ValueError("String is Empty")
    else:
        reversed_string = ''.join(char for char in string[::-1])
        return True if string == reversed_string else False

print(reverseString('ab'))

def stringReverse(string):
    r_string = ""
    for i in string:
        r_string = i + r_string
    return r_string

print(stringReverse('hello'))

def sortString(str):
    return ''.join(sorted(str))