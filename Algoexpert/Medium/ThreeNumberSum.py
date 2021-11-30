# Category - Arrays
def threeNumberSum(array, targetsum):
    array.sort()
    threeNumberList = []
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            for k in range(j+1, len(array)):
                if array[i] + array[j] + array[k] == targetsum:
                    numbers =array[i], array[j], array[k]
                    threeNumberList.append(numbers)
    return threeNumberList

print(threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0))
