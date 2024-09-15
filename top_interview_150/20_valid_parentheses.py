class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = []

        s = list(s)
        for i in s:
            if i in ('(', '[', '{'):
                stack.append(i)
            elif len(stack) == 0:
                return False
            elif i == ')' and stack.pop() != '(':
                return False
            elif i == ']' and stack.pop() != '[':
                return False
            elif i == '}' and stack.pop() != '{':
                return False
        
        if len(stack) != 0:
            return False
        
        return True
