class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        elif x == 1:
            return 1

        l, r = 0, x
        while l <= r:
            mid = l + (r-l)//2
            if mid**2 == x:
                return mid
            elif mid**2 > x:
                r = mid - 1
            else:
                l = mid + 1

        return r
