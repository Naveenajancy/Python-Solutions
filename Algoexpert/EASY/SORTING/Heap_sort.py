# Heap Sort in python


def heapify(arr, n, i):
    # Find largest among root and children
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    # If root is not largest, swap with largest and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)
    # Build max heap
    for i in range(n // 2, -1, -1):
        print(f"heapifying .... {arr}")
        heapify(arr, n, i)
    print(f"first final heapify{arr}")
    for i in range(n - 1, 0, -1):
        # Swap
        print(f"Array ...{arr}")
        arr[i], arr[0] = arr[0], arr[i]
        print(f"Swapping {arr}")
        # Heapify root element
        heapify(arr, i, 0)
        print(f"heapfying after swap {arr}")


arr = [1, 12, 9, 5, 6, 10]
heapSort(arr)
n = len(arr)
print("Sorted array is")
for i in range(n):
    print("%d " % arr[i], end='')