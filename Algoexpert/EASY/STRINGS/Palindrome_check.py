def isPalindrome(string):
        return string == string[::-1]

def reverse(string):
    reverse = ""
    for char in string:
        reverse = char + reverse
        #print(reverse, type(reverse))
    return reverse

#print(isPalindrome('hello'))
print(reverse('jancy'))
