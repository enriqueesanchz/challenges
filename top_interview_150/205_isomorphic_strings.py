class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        chars_a = {}
        chars_b = {}

        for i in range(len(s)):
            if s[i] not in chars_a:
                chars_a[s[i]] = t[i]
            else:
                if chars_a[s[i]] != t[i]:
                    return False

            if t[i] not in chars_b:
                chars_b[t[i]] = s[i]
            else:
                if chars_b[t[i]] != s[i]:
                    return False
        
        return True

