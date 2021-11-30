numberlist = []
for i in range(10):
    numberlist.append(i)

print(numberlist)

for i in range(3):
    print(i, numberlist.pop(i))

print(f"after pop {numberlist}")

numberlist.remove(6)

print(f"remove 6 {numberlist}")

del numberlist[10:10]
print(numberlist)


