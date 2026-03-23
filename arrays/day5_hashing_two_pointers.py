def two_sum(nums,target):
    num_map = {}
    for i in range(len(nums)):
        diff=target-nums[i]
        if diff in num_map:
            return [num_map[diff],i]
        num_map[nums[i]]=i
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
