def caserCipherEncryptor(string, key):
    cipherWord = []
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    new_key = key % 26
    print(f"newKey {new_key} ")
    for character in string:
        cipherLetterValue = alphabet.index(character) + new_key
        print(cipherLetterValue, (cipherLetterValue % 26))
        cipherWord.append(alphabet[cipherLetterValue % 26])

    return ''.join(cipherWord)


print(caserCipherEncryptor("opqrstuv", 100))
print(caserCipherEncryptor("lmn", 2))
