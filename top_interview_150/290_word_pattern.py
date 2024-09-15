class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        chars = {}
        words = {}

        pattern = list(pattern)
        s = s.split(' ')

        n, m = len(pattern), len(s)
        if n != m:
            return False

        for i in range(n):
            if pattern[i] not in chars:
                chars[pattern[i]] = s[i]
            else:
                if chars[pattern[i]] != s[i]:
                    return False
            
            if s[i] not in words:
                words[s[i]] = pattern[i]
            else:
                if words[s[i]] != pattern[i]:
                    return False
        
        return True
