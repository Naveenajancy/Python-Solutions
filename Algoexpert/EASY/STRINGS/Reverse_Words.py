

def reverseWordsInString(string):
    words = []
    startofWord = 0
    for idx in range (len(string)):
        character = string[idx]
        if character == " ":
            words.append(string[startofWord:idx])
            startofWord = idx
        elif string[startofWord] == " ":
            words.append(" ")
            startofWord = idx
    words.append(string[startofWord:])
    reverseList(words)
    return "".join(words)

def reverseList(list):
    start, end = 0, len(list) - 1
    while start < end:
        list[start], list[end] = list[end], list[start]
        start += 1
        end -= 1


print(reverseWordsInString("hello my name is jancy   3"))