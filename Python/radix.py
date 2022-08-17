# Radix Sort

from counting import countingSort

def radixSort(array):
  
    # Find the maximum number to know number of digits
    max1 = max(array)
  
    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1
    while max1 / exp > 1:
        countingSort(array, exp)
        exp *= 10
    return array


x = [3, 6, 324, 764, 14, 7634, 65, 2]
print*(radixSort(x))

# WORK IN PROGRESS