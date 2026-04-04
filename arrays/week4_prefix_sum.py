class Prefixsum:
    def prefix_sum(self,nums):
        prefix=[0]*len(nums)
        prefix[0]=nums[0]
        for i in range(1,len(nums)):
            prefix[i]=prefix[i-1]+nums[i]
        return prefix
    def range_sum(self,prefix,l,r):
        if l==0:
            return prefix[r]
        else:
            return prefix[r]-prefix[l-1]
        
    def subarray_sum(self,nums,k):
        prefix_sum=0
        count=0
        prefix_map={0:1}  # Initialize with prefix sum 0 occurring once
        for num in nums:
            prefix_sum+=num
            if prefix_sum-k in prefix_map:
                count+=prefix_map[prefix_sum-k]
            prefix_map[prefix_sum]=prefix_map.get(prefix_sum,0)+1
        return count
    
    def longest_subarray(self,nums,k):
        prefix_sum=0
        max_len=0
        prefix_map={}
        for i in range(len(nums)):
            prefix_sum+=nums[i]
            if prefix_sum == k:
                max_len=i+1
            if prefix_sum-k in prefix_map:
                max_len=max(max_len,i-prefix_map[prefix_sum-k])
            if prefix_sum not in prefix_map:
                prefix_map[prefix_sum]=i
        return max_len
    
    
    def subarray_divisible_by_k(self,nums,k):
        prefix_sum=0
        count=0
        reminder_map={0:1}
        for num in nums:
            prefix_sum+=num
            rem=prefix_sum%k
            if rem<0:
                rem+=k
            
            if rem in reminder_map:
                count+=reminder_map[rem]
            
            reminder_map[rem]=reminder_map.get(rem,0)+1
        return count
        
        
    def count_equal_0_1(self,nums):
        prefix_sum=0
        count=0
        prefix_map={0:1}
        for num in nums:
            if num==0:
                prefix_sum+= -1
            else:
                prefix_sum+=1
            if prefix_sum in prefix_map:
                count+=prefix_map[prefix_sum]
            prefix_map[prefix_sum]=prefix_map.get(prefix_sum,0)+1
        return count
        
        
obj=Prefixsum()
nums=[1,2,3,4,5]
prefix=obj.prefix_sum(nums)
print(prefix)  # Output: [1, 3, 6, 10, 15]
print(obj.range_sum(prefix,1,3))  # Output: 9 (2+3+4)
nums2=[1,1,1]
k=2
print(obj.subarray_sum(nums2,k))  # Output: 2 (subarrays [1,1] and [1,1])
nums3=[1,-1,5,-2,3]
k2=3
print(obj.longest_subarray(nums3,k2))  # Output: 4 (subarray [1, -1, 5, -2])
nums4=[4,5,0,-2,-3,1]
k3=5
print(obj.subarray_divisible_by_k(nums4,k3))  # Output: 7
nums5=[0,1,0,1,0]
print(obj.count_equal_0_1(nums5))  # Output: 6 (subarrays [0,1], [1,0], [0,1], [0,1,0], [1,0,1], [0,1,0,1])