def isValid(s):
        valid_pairs = {"(":")", "[":"]","{":"}"}
        stack = []
        for char in s:
                if char in valid_pairs:
                        stack.append(char)
                else:
                        if not stack:
                                return False
                        top_opener = stack[-1]
                        if valid_pairs[top_opener] == char:
                                stack.pop()
                        else:
                                return False
        return True
                                
                
print(isValid("()"))
print(isValid("["))
print(isValid("(){}}{"))
print(isValid("()[]{}"))