import string

def alphabet_position(text):
    return ' '.join(str(string.ascii_lowercase.index(i) + 1) for i in text.lower() if i.isalpha())

'''
    #position = []
    #position = ""
    #words = text.lower()
    #for i in text.lower():
        #if i.isalpha():
        position = ' '.join(str((string.ascii_lowercase.index(i)) + 1))
        #pos = ' '.join((str(pos) for pos in position))
'''


result = alphabet_position("ABCDEFGHIJKLMNOPQRSTUVWXYZ.123")
print(f"Alphbet postition : {result}")