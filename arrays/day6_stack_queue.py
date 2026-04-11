from collections import deque


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
    
    def largest_rectangle_area(self,heights):
        maxarea=0
        stack=[]
        for i,h in enumerate(heights):
            start=i
            while stack and stack[-1][1]>h:
                index,height=stack.pop()
                maxarea=max(maxarea,height*(i-index))
                start=index
            stack.append((start,h))
        for i,h in stack:
            maxarea=max(maxarea,h*(len(heights)-i))
        return maxarea
    
    
obj=solution()
s="()[]{}"
print(obj.is_valid(s))  # Output: True
nums=[4,5,2,10,8]
print(obj.next_greater(nums))  # Output: [5, 10, 10, -1, -1]
print(obj.next_smaller(nums))  # Output: [2, 2, -1, 8, -1]
print(obj.largest_rectangle_area([2, 1, 5, 6, 2, 3]))  # Output: 10
    
class minstack:
    def __init__(self):
        self.stack=[]
        self.min_stack=[]
        
    def push(self,x):
        self.stack.append(x)
        if not self.min_stack or x<=self.min_stack[-1]:
            self.min_stack.append(x)
            
    def pop(self):
        if self.stack:
            if self.stack[-1]==self.min_stack[-1]:
                self.min_stack.pop()
            self.stack.pop()
            
    def top(self):
        if self.stack:
            return self.stack[-1]
        
    def get_min(self):
        if self.min_stack:
            return self.min_stack[-1]
    


obj2=minstack()
obj2.push(5)
obj2.push(3)
obj2.push(2)
obj2.push(4)
obj2.push(7)
print(obj2.get_min()) # Output: 2
obj2.pop()
print(obj2.get_min()) # Output: 2
obj2.pop()
obj2.pop()
print(obj2.get_min()) # Output: 3


class queue:
    def __init__(self):
        self.queue=deque()
        
    def enqueue(self,x):
        self.queue.append(x)
        print(x,"added")
        
    def dequeue(self):
        if self.queue:
            return self.queue.popleft()
        return "queue is empty"
    
    def peek(self):
        if self.queue:
            return self.queue[0]
        return "queue is empty"
    
    def is_empty(self):
        return len(self.queue)==0
obj3=queue()
obj3.enqueue(1)
obj3.enqueue(2)
obj3.enqueue(3)
print(obj3.dequeue())  # Output: 1
print(obj3.peek())     # Output: 2

class circularqueue:
    def __init__(self,size):
        self.size=size
        self.queue=[None]*size
        self.front=-1
        self.rear=-1
        
    def enqueue(self,x):
        if (self.rear+1)%self.size==self.front:
            return "queue is full"
        if self.front==-1:
            self.front=0
        self.rear=(self.rear+1)%self.size
        self.queue[self.rear]=x
        print(x,"added")
        
    def dequeue(self):
        if self.front==-1:
            print("queue is empty")
            return
        val=self.queue[self.front]
        if self.front==self.rear:
            self.front=-1
            self.rear=-1
        else:
            self.front=(self.front+1)%self.size
        return val,"removed"
    
    def display(self):
        if self.front==-1:
            print("queue is empty")
            return
        i=self.front
        while True:
            print(self.queue[i],end=" ")
            if i==self.rear:
                break
            i=(i+1)%self.size
        print()
obj4=circularqueue(5)
obj4.enqueue(1)
obj4.enqueue(2)
obj4.enqueue(3)
obj4.enqueue(4)
obj4.enqueue(5)
obj4.enqueue(6)  # Output: "queue is full"
obj4.display()  # Output: 1 2 3 4 5
print(obj4.dequeue())  # Output: (1, "removed")
print(obj4.dequeue())  # Output: (2, "removed")
obj4.display()  # Output: 3 4 5

class max:
    def sliding_window_max(self,k,nums):
        res=[]
        dq=deque()
        for i in range(len(nums)):
            if dq and dq[0]<i-k+1:
                dq.popleft()
            while dq and nums[i]>nums[dq[-1]]:
                dq.pop()
            dq.append(i)
            if i>=k-1:
                res.append(nums[dq[0]])
        return res
    
obj5=max()
nums=[1,3,-1,-3,5,3,6,7]
k=3
print(obj5.sliding_window_max(k,nums))  # Output: [3, 3, 5, 5, 6, 7]