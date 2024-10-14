class Solution:
    def isHappy(self, n: int) -> bool:
        
        def nextn(n):
            res = 0
            while n:
                temp = n%10
                n = n//10
                res += temp**2

            return res

        fast = slow = n
        while True:
            slow = nextn(slow)
            fast = nextn(fast)
            fast = nextn(fast)

            if slow == fast:
                break

        return fast == 1
