class stack:
    def __init__(self):
        self.stack=[]
    def push(self,x):
        self.stack.append(x)
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "stack is empty"
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return "stack is empty"
    def is_empty(self):
        return len(self.stack)==0
    
    
obj=stack()
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
print(obj.peek())
print(obj.pop())
print(obj.peek())

class solution:
    def is_valid(self,s):
        stack=[]
        mapping={')':'(',']':'[','}':'{'}
        for ch in s:
            if ch in mapping:
                if not stack or stack[-1]!=mapping[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)
        return len(stack)==0
    
    def next_greater(self,nums):
        res=[-1]*len(nums)
        stack=[]
        for i in range(len(nums)):
            while stack and nums[i]>nums[stack[-1]]:
                index=stack.pop()
                res[index]=nums[i]
            stack.append(i)
        return res
    
    def next_smaller(self,nums):
        res=[-1]*len(nums)
        stack=[]
        for i in range(len(nums)):
            while stack and nums[i]<nums[stack[-1]]:
                index=stack.pop()
                res[index]=nums[i]
            stack.append(i)
        return res
    
obj=solution()
s="()[]{}"
print(obj.is_valid(s))  # Output: True
nums=[4,5,2,10,8]
print(obj.next_greater(nums))  # Output: [5, 10, 10, -1, -1]
print(obj.next_smaller(nums))  # Output: [2, 2, -1, 8, -1]