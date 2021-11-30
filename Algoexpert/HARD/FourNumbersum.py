def fourNumberSum(array, targetSum):
    numberPair = {}
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            numberPair[array[i], array[j]] = array[i] +array[j]
    numberValues = list(numberPair.values())
    for i in range(len(numberValues) -1):
        for j in range(len(numberValues)):
            if numberValues[i] + numberValues[j] == targetSum:
                p


    return numberPair
print(fourNumberSum([7, 6, 4, -1, 1, 2], 16))

