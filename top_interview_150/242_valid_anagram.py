class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)

        if n != m:
            return False
            
        chars = [0] * 26
        for i in range(n):
            idx = ord(s[i])-97
            chars[idx] += 1
            idx = ord(t[i])-97
            chars[idx] -= 1

        for i in chars:
            if i != 0:
                return False

        return True

"""
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
"""
