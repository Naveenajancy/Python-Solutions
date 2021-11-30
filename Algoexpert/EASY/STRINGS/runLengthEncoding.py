"""
from collections import OrderedDict
# 10/15 test cases are failed
    inout : {
  "string": "[(aaaaaaa,bbbbbbb,ccccc,dddddd)]"
}
    output : "1[1(7a1,7b1,5c1,6d1)1]"
    My output : "1[1(7a3,7b5c6d1)1]"
    
def runLengthEncoding(string):
    unique_characters = list(OrderedDict.fromkeys(string))
    print(unique_characters)
    encoding = []
    for i in unique_characters:
        count_character = string.count(i)
        if count_character > 9:
            division = count_character // 9
            reminder = count_character % 9
            long_length = "9" + i
            division_count = division * long_length
            remainder_count = str(reminder) + i
            sum = division_count + remainder_count
            encoding.append(sum)
        else:
            sum = str(count_character) + i
            encoding.append(sum)
    return ''.join(encoding)

print(runLengthEncoding("[(aaaaaaa,bbbbbbb,ccccc,dddddd)]"))
"""

def runLengthEncoding(string):
    # the input is guaranteed to be non empty
    # the first run will be of at least length 1
    encodedStringCharacters = []
    currentRunLength = 1
    for i in range(1, len(string)):
        current_character = string[i]
        previous_character = string[i-1]
        if current_character != previous_character or currentRunLength == 9:
            encodedStringCharacters.append(str(currentRunLength))
            encodedStringCharacters.append(previous_character)
            currentRunLength = 0

        currentRunLength += 1

    encodedStringCharacters.append(str(currentRunLength))
    encodedStringCharacters.append(string[len(string)-1])

    return ''.join(encodedStringCharacters)

print(runLengthEncoding("1A2BB3CCC4DDDD"))







