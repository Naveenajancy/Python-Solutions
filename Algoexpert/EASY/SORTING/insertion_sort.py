def insertions_sort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array [j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
            j -= 1
    return array

print(insertions_sort([-1,2,6,8,0,2,1]))