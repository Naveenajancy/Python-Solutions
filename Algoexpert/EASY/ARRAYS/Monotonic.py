# O(n) Time | O(1) Space
def isMonotonic(array):
    isNonDecreasing = True
    isNonIncreasing = True
    for i in range(1, len(array)):
        if array[i] > array[i-1]:
            isNonDecreasing = False
        if array[i] < array[i-1]:
            isNonIncreasing = False
    print(isNonIncreasing, isNonDecreasing)
    return isNonIncreasing or isNonDecreasing

print(isMonotonic([-1, -5, -10, -1100, -1100, -1101]))
print(isMonotonic([]))
print(isMonotonic([1, 2, 3, 5,  6, 8]))
print(isMonotonic([10, 9, 8, 7, 6, 5]))
print(isMonotonic([11,2,3,4,10,1]))
print(isMonotonic([1,1,1,1,1,]))
print(isMonotonic([1]))
print(isMonotonic([1,2,2,3,3,4,4]))
