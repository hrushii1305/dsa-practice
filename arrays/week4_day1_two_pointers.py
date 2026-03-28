class twopointers:
    def pair_sum(self, arr, target):
        left = 0
        right = len(arr) - 1

        while left < right:
            current_sum = arr[left] + arr[right]

            if current_sum == target:
                return [left, right]
            elif current_sum < target:
                left += 1
            else:
                right -= 1

        return None  # Return None if no pair is found
    
    
    def remove_duplicates(self,nums):
        if not nums:
            return []
        slow=0
        for fast in range(1,len(nums)):
            if nums[slow]!=nums[fast]:
                slow+=1
                nums[slow]=nums[fast]
        return nums[:slow+1]
    
    def move_zeros(self,nums):
        slow=0
        for fast in range(len(nums)):
            if nums[fast]!=0:
                nums[slow],nums[fast]=nums[fast],nums[slow]
                slow+=1
        return nums
    def water_container(self,height):
        left=0
        right-len(height)-1
        res=0
        while left<right:
            area=(right-left)*min(height[left],height[right])
            res=max(res,area)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return res

obj=twopointers()
print(obj.pair_sum([1, 2, 3, 4, 5], 9))  # Output: [3, 4]
print(obj.remove_duplicates([1, 1, 2, 2, 3, 3]))  # Output: [1, 2, 3]
print(obj.move_zeros([0, 1, 0, 3, 12]))  # Output: [1, 3, 12, 0, 0]
print(obj.water_container([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # Output: 49
