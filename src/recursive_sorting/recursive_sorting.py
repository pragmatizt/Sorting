# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(array_left, array_right):
    elements = len(array_left) + len(array_right)
    merged = [0] * elements  # initializing an array

    # Track index for our left and right arrays
    left_index = 0
    right_index = 0
    # for loop in range of merge array
    # it also needs to start with 0
    for merge_index in range(0, len(merged)):
        # each index of final merge array
        # we need to find right element to be plugged back in
        # position 0 of left array and right array, which value is smaller
        # now we switch elements out when index of left is higher than its total length

        if left_index >= len(array_left):
            merged[merge_index] = array_right[right_index]
            right_index += 1

        # check the right array if its index exceeds to length swap
        elif right_index >= len(array_right):
            merged[merge_index] = array_left[left_index]
            left_index += 1
        
        # Check elements at given respective indexes and find smaller one and store in merged[merge_index]
        elif array_left[left_index] < array_right[right_index]:
            merged[merge_index] = array_left[left_index]
            left_index += 1
            # increase left index as this element is stored inside merged

        # Check elements at given respective indices and find smaller
        # and store in merged[merge_index]
        elif array_left[left_index] > array_right[right_index]:
            merged[merge_index] = array_right[right_index]
            # increase right index as this element is smallest and 
            # stored in merge
            right_index += 1

    return merged


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # We need the middle point of the given array
    # so that we know where to split it
    half = len(arr)//2
    left_half = arr[:half] 
    right_half = arr[half:]

    
    # Base Case
    if len(arr) == 1:
        return arr
    else:
        leftside_recursion = merge_sort(left_half)
        rightside_recursion = merge_sort(right_half)
        new_merge = merge(leftside_recursion, rightside_recursion)
        return new_merge

    # return arr
array = [4, 5, 8, 9, 3, 7]
print(merge_sort(array))























# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
