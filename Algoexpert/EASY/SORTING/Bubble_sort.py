def bubblesort(array):
    iterations = 0
    has_swapped = True
    while has_swapped:
        has_swapped = False
        for j in range(0, len(array) - 1 - iterations):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                has_swapped = True
        iterations += 1
    return array

print(bubblesort([8, 5, 2, 9, 6, 3]))
