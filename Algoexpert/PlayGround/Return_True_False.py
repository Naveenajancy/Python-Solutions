def containsNvalue(array, n):
    return True if n in array else False

print(containsNvalue([12,34,5,1], 1))

def sorting(array):
    array.sort()
    print(array)
    #reverse = reversed(array)
    print(sorted(array, reverse=True))
    print(array)

array = [45, 5, 2, 1, 40, 100]
sorting(array)