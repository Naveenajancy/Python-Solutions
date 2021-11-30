def generateDocument(characters, document):
    createDocument = True
    unique_elements = set(document)
    print(unique_elements)
    for char in unique_elements:
        print("in for loop")
        print(f"DC : CC  {document.count(char)} {characters.count(char)}")
        if document.count(char) > characters.count(char):
            createDocument = False
    return createDocument

print(generateDocument("aaa", ""))
