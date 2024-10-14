from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        def resolve(x, y, oper):
            if oper == '+': return x+y
            elif oper == '-': return x-y
            elif oper == '*': return x*y
            return int(x/y)
        
        stack = []
        n = len(tokens)
        for i in range(n):
            token = tokens[i]
            if len(token) == 1 and not token.isdigit():
                y = stack.pop()
                x = stack.pop()
                stack.append(resolve(x, y, token))
            else:
                stack.append(int(token))

        return stack.pop()
