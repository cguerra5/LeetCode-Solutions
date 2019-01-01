
def smallestLargerValue(arr, target):
    """
    For a sorted array arr, returns the index of the smallest value that
    is greater than target using a binary search. If dupicates of this
    value exist, then it finds the leftmost occurence.
    """
    left_bound = 0
    right_bound = len(arr)
    pivot = len(arr) // 2
    
    while (left_bound < right_bound):
        if (arr[pivot] > target):
            right_bound = pivot - 1
        elif (arr[pivot] <= target):
            # If the target equals the pivot, keep searching the right side
            # in case of dupicates
            left_bound = pivot + 1
        pivot = (left_bound + right_bound) // 2
    
    if arr[pivot] > target:
        return pivot
    else:
        return pivot + 1

def binarySearch(arr, target):
    """
    For a sorted array arr, returns the index of the smallest value that
    is greater than target using a binary search. If dupicates of this
    value exist, then it finds the leftmost occurence.
    """
    left_bound = 0
    right_bound = len(arr)
    pivot = len(arr) // 2
    
    while (left_bound < right_bound):
        if (arr[pivot] > target):
            right_bound = pivot - 1
        elif (arr[pivot] < target):
            left_bound = pivot + 1
        else:
            return pivot
        pivot = (left_bound + right_bound) // 2
    
    return None

