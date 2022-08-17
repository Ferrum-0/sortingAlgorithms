# Bubble Sort

def bubbleSort(array):
    # Iterating through the array.
    for i in range(len(array)):
        for j in range(len(array) - 1):
            # Swapping the values of the array.
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    # Returning the sorted array.
    return array