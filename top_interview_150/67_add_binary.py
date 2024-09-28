class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = list(a)
        b = list(b)
        res = ""
        carry = 0
        while a or b:
            x = int(a.pop()) if a else 0
            y = int(b.pop()) if b else 0 
            res += str((x+y+carry)%2)
            carry = (x+y+carry)//2

        if carry:
            res += str(carry)

        return res[::-1]
