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

def count_occurrences(arr, target):
    first=first_occurrence(arr, target)
    if first==-1:
        return 0
    last=last_occurrence(arr, target)
    return last-first+1

def sqrt_binary(n):
    left=0
    right=n
    ans=0
    while left<=right:
        mid=left+right//2
        if mid*mid==n:
            return mid
        elif mid*mid<n:
            ans=mid
            left=mid+1
            
        else:
            right=mid-1
    return ans

def lower_bound(arr,target):
    left=0
    right=len(arr)-1
    ans=len(arr)
    while left<=right:
        mid=left+right//2
        if arr[mid]>=target:
            ans=mid
            right=mid-1
        else:
            left=mid+1
    return ans


        
# Example usage:
arr = [1, 2, 3, 4, 5, 5, 5, 6, 7]
target = 5
print("Binary Search:", binary_search(arr, target))  # Output: Index of target (could be any of the indices where 5 is located)
print("First Occurrence:", first_occurrence(arr, target))  # Output: Index of the first occurrence of target (4)
print("Last Occurrence:", last_occurrence(arr, target))  # Output: Index of the last occurrence of target (6)
print("Count Occurrences:", count_occurrences(arr, target))  # Output: Count of target in the array (3)
print("Square Root:", sqrt_binary(16))  # Output: 4
print("Square Root:", sqrt_binary(20))  # Output: 4
print("Lower Bound:", lower_bound(arr, 5))  # Output: 4 (index of the first occurrence of 5)