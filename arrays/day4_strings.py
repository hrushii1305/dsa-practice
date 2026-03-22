def reverse_string(s):
    result=""
    for ch in s:
        result=ch+result
    return result

def palindrome(s):
    left=0
    right=len(s)-1
    while left<right:
        if s[left]!=s[right]:
            return False
        left+=1
        right-=1
    return True

def valid_palindrome(s):
    left=0
    right=len(s)-1
    while left<right:
        while left<right and not s[left].isalnum():
            left+=1
        while left<right and not s[right].isalnum():
            right-=1
        if s[left].lower()!=s[right].lower():
            return False
        left+=1
        right-=1
    return True

def char_frequency(s):
    freq={}
    for ch in s:
        freq[ch=freq.get(ch,0)+1]
    return freq

def first_unique_char(s):
    freq={}
    for ch in s:
        freq[ch]=freq.get(ch,0)+1
    for ch in s:
        if freq[ch]==1:
            return ch
    return None
print(reverse_string("hello"))
print(palindrome("racecar"))
print(valid_palindrome("A man, a plan, a canal: Panama"))
print(char_frequency("hello world"))
print(first_unique_char("leetcode"))


