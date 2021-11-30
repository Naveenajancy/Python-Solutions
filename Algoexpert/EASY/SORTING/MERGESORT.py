# O(n Log(n)) time | O(nLOg(n)) Space

def mergeSort(array):
    print("HELLO I DIVIDE TO GET BASE CASE")
    print(f"gieven array {array}")
    if len(array) == 1:
        print(f"Length of array is 1 return Array is {array}")
        return array
    print("The length of array is great than 1 so divide")
    middleIdx = len(array) // 2
    print(f"middle index {middleIdx}")
    leftHalf = array[:middleIdx]
    print(f"leftHalf {leftHalf}")
    rightHalf = array[middleIdx:]
    print(f"rightHalf {rightHalf}")
    return mergeSortedArrays(mergeSort(leftHalf), mergeSort(rightHalf))
    #return mergeSortedArrays(mergeSort(rightHalf), mergeSort(leftHalf))

def mergeSortedArrays(leftHalf, rightHalf):
    print("HELLO I AM A MERGER")
    sortedArray = [None] * (len(leftHalf) + len(rightHalf))
    print(f"Sorted array in the beginning {sortedArray}   leftHalf: {leftHalf} lengthL: {len(leftHalf)} rightHalf: {rightHalf} lengthR: {len(rightHalf)}")
    i = j = k = 0
    print(f"VALUES of i: {i} j: {j} k: {k}")
    while i < len(leftHalf) and j < len(rightHalf):
        if leftHalf[i] <= rightHalf[j]:
            sortedArray[k] = leftHalf[i]
            print(f"sorted array in left[i] < right [j] {sortedArray}")
            i += 1
        else:
            sortedArray[k] = rightHalf[j]
            print(f"sorted array in left[i] > right [j] {sortedArray}")
            j += 1
        k += 1
    while i < len(leftHalf):
        print(f"i < len(halfHalf) i {i} {len(leftHalf)} leftHalfvalues : {leftHalf}")
        sortedArray[k] = leftHalf[i]
        i += 1
        k += 1
    while j < len(rightHalf):
        print(f"j < len(rightHalf) j {j} {len(rightHalf)} rightHalfvalues : {rightHalf}")
        sortedArray[k] = rightHalf[j]
        j += 1
        k += 1
    print(f"sortedArray in the end {sortedArray}")
    return sortedArray

mergeSort([8, 2, 6, 1, 10, 0, 5])
    
    