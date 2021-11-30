def selectionSort(array):
    swap_count = 0
    for i in range(len(array)):
        print(f"i {i}")
        min_idx = i
        for j in range(i+1, len(array)):
            print(f"j {j}")
            if array[min_idx] > array[j]:
                min_idx = j

        print(array)

        array[i], array[min_idx] = array[min_idx], array[i]
        swap_count += 1
        #print(swap_count, array)
    return array

print(selectionSort([64, 23, 44, 100, 11, 0]))