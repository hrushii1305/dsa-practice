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
        res=0
        current_sum=0
        prefix_sums={0:1}
        for n in nums:
            current_sum+=n
            diff=current_sum-k
            res+=prefix_sums.get(diff,0)
            prefix_sums[current_sum]=prefix_sums.get(current_sum,0)+1
        return res
    
        
        
        
obj=Prefixsum()
nums=[1,2,3,4,5]
prefix=obj.prefix_sum(nums)
print(prefix)  # Output: [1, 3, 6, 10, 15]
print(obj.range_sum(prefix,1,3))  # Output: 9 (2+3+4)
nums2=[1,1,1]
k=2
print(obj.subarray_sum(nums2,k))  # Output: 2 (subarrays [1,1] and [1,1])