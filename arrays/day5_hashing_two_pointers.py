def two_sum(nums,target):
    num_map = {}
    for i,num in enumerate(nums):
        diff=target-num
        if diff in num_map:
            return [num_map[diff],i]
        num_map[num]=i
    return []

def is_anagram(s,t):
    if len(s)!=len(t):
        return False
    count={}
    for ch in s:
        count[ch]=count.get(ch,0)+1
    for ch in t:
        if ch not in count or count[ch]==0:
            return False
        count[ch]-=1
    return True

def pair_with_target(arr,target):
    left=0
    right=len(arr)-1
    while left<right:
        current_sum=arr[left]+arr[right]
        if current_sum==target:
            return [left,right]
        elif current_sum<target:
            left+=1
        else:
            right-=1
    return []

def subarray_sum(nums,k):
    prefix_sum=0
    count=0
    prefix_map={0:1}
    for num in nums:
        prefix_sum+=num
        previous_sum=prefix_sum-k
        if previous_sum in prefix_map:
            count+=prefix_map[previous_sum]
        prefix_map[prefix_sum]=prefix_map.get(prefix_sum,0)+1
    return count

def longest_subarray(nums,k):
    prefix_sum=0
    max_length=0
    prefix_map={}
    for i in range(len(nums)):
        prefix_sum+=nums[i]
        if prefix_sum==k:
            max_length=i+1
        elif prefix_sum-k in prefix_map:
            max_length=max(max_length,i-prefix_map[prefix_sum-k])
        if prefix_sum not in prefix_map:
            prefix_map[prefix_sum]=i
    return max_length

print(two_sum([2,7,11,15],9))
print(is_anagram("listen","silent"))
print(pair_with_target([1,2,3,4,5],7))
print(subarray_sum([1,1,1],2))
print(longest_subarray([1,-1,5,-2,3],3))
