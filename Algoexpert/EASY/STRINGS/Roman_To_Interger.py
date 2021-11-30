def romanToInt(str):
    romanKeyValue = {"I": 1, "V": 5, "X": 10, "L": 50,
                     "C": 100, "D": 500, "M": 1000, "CM":900,
                     "CD":400, "XC":90, "XL":40, "IX":9, "IV":4}
    integerValue = 0
    specialsLetters = {"CD", "CM", "XC", "xL", "IX", "IV"}
    for i in specialsLetters:
        if i in str:
            integerValue += romanKeyValue[i]
            str = str.replace(i, "")
    if str:
        print("hi")
        for i in str:
            integerValue += romanKeyValue[i]
    return integerValue

A = "IIIII"
B = "CDCM"
C = "CDCD"
D = "IV"
print(romanToInt(A))
print(romanToInt(B))
print(romanToInt(C))
print(romanToInt(D))





"""
def romanToInteger(str):
    romanKeyValue = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    #etters = str.split(' ')
    integerValue = 0
    idx = len(str) - 1
    while idx > -1:
        char = string[idx]
        if (char == 'I' and idx != 0 and str[i+1] == 'V' or 'X'):
            print("hi 1")
            integerValue += romanKeyValue[str[i+1]] - romanKeyValue[str[i]]
            i += 2
        elif str[i] == 'X' and str[i+1] == 'L' or 'C':
            print("hi 2")
            integerValue += romanKeyValue[str[i + 1]] - romanKeyValue[str[i]]
            i += 2
        elif str[i] == 'C' and str[i+1] == 'D' or 'M':
            print("hi 3")
            integerValue += romanKeyValue[str[i + 1]] - romanKeyValue[str[i]]
            i += 2

        print("Im at end")
        integerValue += romanKeyValue[str[i]]
    print("final")
    return integerValue

print(romanToInteger("III"))
"""