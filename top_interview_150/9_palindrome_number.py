class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        curr = x
        rev = 0
        while curr:
            rev = rev * 10 + curr % 10
            curr = curr // 10

        return x == rev
