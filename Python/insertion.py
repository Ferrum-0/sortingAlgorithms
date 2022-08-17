# Insertion Sort

def insertionSort(array):
    # Iterating through the array starting at the second element.
    for i in range(1, len(array)): 
        # Setting the key to the value of the current element in the array.
        key = array[i]
        # Setting the value of j to the index of the previous element in the array.
        j = i-1
        # This is the while loop that is used to iterate through the array. The while loop will
        # continue to run as long as the value of j is greater than or equal to 0 and the value of key
        # is less than the value of the element at the index of j.
        while j >=0 and key < array[j]:
                # This is the line of code that is used to shift the elements in the array.
                array[j+1] = array[j]
                j -= 1
        # This line of code is used to insert the key into the correct position in the array.
        array[j+1] = key
    return array