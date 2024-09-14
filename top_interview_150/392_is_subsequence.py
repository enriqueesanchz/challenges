class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(s)
        if n == 0:
            return True
        m = len(t)
        if m < n:
            return False
        
        i = 0
        j = 0
        while i < n and j < m:
            if s[i] == t[j]:
                i += 1
            j += 1
        
        if n == i:
            return True

        return False
