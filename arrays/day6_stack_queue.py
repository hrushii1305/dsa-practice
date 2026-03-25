def is_valid(s):
    stack=[]
    mapping={")":"(","}":"{","]":"["}
    for ch in s:
        if ch in mapping:
            if stack and stack[-1]==mapping[ch]:
                stack.pop()
            else:
                return False
        else:
            stack.append(ch)
    return True if not stack else False

print(is_valid("()[]{}"))