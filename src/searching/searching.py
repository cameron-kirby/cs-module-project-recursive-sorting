# NOTE: GP showed cool way to do it without tracking/passing in start and end points of search partition

# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    middle = (start+end)//2
    # Check if empty
    if len(arr) == 0:
        return -1
    # Check if start and end have met
    if start >= end:
        return -1
    # Check best case
    if arr[middle] == target:
        return middle
    # Do recursive search
    else:
        if target > arr[middle]:
            start = middle - 1
        elif target < arr[middle]:
            end = middle + 1
    
        return binary_search(arr, target, start, end)



# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively

def agnostic_binary_search(arr, target):
    # Your code here
    pass

