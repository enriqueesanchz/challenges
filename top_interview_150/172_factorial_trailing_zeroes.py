class Solution:
    def trailingZeroes(self, n: int) -> int:
        
        count = 0
        x = 5
        while n >= x:
            count += n // x
            x *= 5

        return count
