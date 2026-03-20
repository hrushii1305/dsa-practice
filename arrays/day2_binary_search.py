def binary_search(arr, target):
    left=0
    right=len(arr)-1
    while left<=right:
        mid=left+right//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return -1

def first_occurrence(arr, target):
    left=0
    right=len(arr)-1
    result=-1
    while left<=right:
        mid=left+right//2
        if arr[mid]==target:
            result=mid
            right=mid-1
        elif arr[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return result

def last_occurrence(arr, target):
    left=0
    right=len(arr)-1
    result=-1
    while left<=right:
        mid=left+right//2
        if arr[mid]==target:
            result=mid
            left=mid+1
        elif arr[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return result

# Example usage:
arr = [1, 2, 3, 4, 5, 5, 5, 6, 7]
target = 5
print("Binary Search:", binary_search(arr, target))  # Output: Index of target (could be any of the indices where 5 is located)
print("First Occurrence:", first_occurrence(arr, target))  # Output: Index of the first occurrence of target (4)
print("Last Occurrence:", last_occurrence(arr, target))  # Output: Index of the last
