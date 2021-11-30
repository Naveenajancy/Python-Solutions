def threeForLoop(array):
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            for k in range(j+1, len(array)):
                print(f"i, j ,k  {i} {j} {k}")

def twoForLoop(array):
    for i in range(len(array)-2):
        for j in range(i+1, len(array)):
            print(f"i, j {i} {j}")


def twoArrayLoops(arrayOne, arrayTwo):
    numberPair = {}
    minKey = ''
    minValuePositive = float('inf')
    minValueNegative = float('-inf')

    for i in range(len(arrayOne)):
        for j in range(len(arrayTwo)):
            difference = abs(arrayOne[i] - arrayTwo[j])
            #print(f"{arrayOne[i]} -  {arrayTwo[j]} = {difference}")
            numberPair[arrayOne[i], arrayTwo[j]] = difference
    minValue = min([x for x in numberPair.values()])
    '''
    for k, v in numberPair.items():
        if v > minValuePositive:
            #minValuePositive = v
            minKey = k
        elif v < minValueNegative:
            minKey = k

    print(minKey)
    
    '''
    """
    print(len(minValue))
    if len(minValue) != 0:
        smallestdiff = min(minValue)
    else:
        smallestdiff = min(x for x in numberPair.values())
       """

    #print (f" smallestdiff {smallestdiff}")
    result = [k for k,v in numberPair.items() if v == minValue]

    print(result)
    #minValue = list(filter(lambda )


twoArrayLoops([10, 0, 20, 25, 2200], [1005, 1006, 1014, 1032, 1031])
#twoArrayLoops([10, 0, 20, 25], [1005, 1006, 1014, 1032, 1031])
#twoArrayLoops([-10, -20 , -30], [-1, -2, -3])
#twoArrayLoops([-1, 5, 10, 20, 28, 3], [26, 134, 15, 17])
#twoForLoop([0,1,2,3,4,5])
#threeForLoop([0,1,2,3,4])
