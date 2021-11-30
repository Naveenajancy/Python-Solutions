#write a function takes array and returns squared array
def SortedSquaredArray(array):
    sortedlist = []
    for i in array:
        sortedlist.append(i**2)
    return sorted(sortedlist, reverse=True)

def sortedSquaredArray(array):
     squaredArray = list(map(lambda x:x**2, array))
     return sorted(squaredArray)

print(sortedSquaredArray([-5, -4, -3, -2, -1]))

print(sortedSquaredArray([-10, -5, 0, 5, 10]))

#print(SortedSquaredArray([1,4,5,6,8,3,2]))

#print(SortedSquaredArray([-2, -1]))

