def max_sum_subarray(arr,k):
    window_sum=sum(arr[:k])
    max_sum=window_sum
    for i in range(k,len(arr)):
        window_sum+=arr[i]
        window_sum-=arr[i-k]
        max_sum=max(max_sum,window_sum)
    return max_sum

def longest_unique_substring(s):
    char_set=set()
    max_length=0
    left=0
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left+=1
        char_set.add(s[right])
        max_length=max(max_length,right-left+1)
    return max_length


def min_subarray_sum(arr,target):
    left=0
    window_sum=0
    min_len=float('inf')
    for right in range(len(arr)):
        window_sum+=arr[right]
        while window_sum>=target:
            window_sum-=arr[left]
            min_len=min(min_len,right-left+1)
            left+=1
        
    return min_len if min_len!=float('inf') else 0



print(max_sum_subarray([1,3,2,5,1,5,4,3],3))     
print(longest_unique_substring("abcabcbb"))
print(min_subarray_sum([2,1,2,3,1],5))