def firstnonRepeatingChracter(string):
    iterations = 0
    print(len(string))
    if len(string) > 0:
        for character in string:
            print(character, iterations)
            if string.count(character) == 1:
                return string.index(character)
            elif len(string)-1 == iterations:
                return -1
            else:
                iterations += 1
    else:
        return -1
    #print(iterations)

print(firstnonRepeatingChracter("aabcahhcdr"))



