def generatelist_tuple():
    data = input("Enter the number\n")
    l = data.split(',')
    t = tuple(l)
    print(f"l: {l} t: {t}")

num = "12,34,45,65,768,100"
#print(type(num))
generatelist_tuple()