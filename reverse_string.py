def reverse(s):
    str = ""
    for i in s:
        str = i + str
        print(f"i is {i} string {str}")
    return str

def reverse_slice(s):
    return s[::-1]

reverse(['10','11','44','232'])
output = reverse_slice(['10','11','44','232'])
print(f"The reverse string using slice operator is:{output}", end="")