# TO-DO: Complete the selection_sort() function below 
"""Divides list into two parts sorted on left; unsorted
on right.  
It uses two pointers: current item, current minimum.
Current item traverses - identifies lowest, then marks it with
"current minimum".  That then gets shifted back.
"""
def selection_sort(arr):
    # Traverse through all array elements
    for i in range(len(arr)):

        # Find the minimum element in remaining
        # unsorted array
        min_index = i   # min index is unsorted array
        for j in range(i+1, len(arr)):  # j is a pointer to next element - remaining unsorted
            if arr[min_index] > arr[j]: # if unsorted > sorted
                min_index = j           # set unsorted = sorted (???)

        # Swap the found minimum element with
        # the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

# TO-DO:  implement the Bubble Sort function below
"""Bubble Sort repeatedly swaps the adjacent elements
if they are in the wrong order; the biggest number naturally
bubbles to the last spot
"""
def bubble_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n): 

        # Last i elements are already in place
        for j in range(0, n-i-1):   # j is 

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j] # Swap occurs here

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr