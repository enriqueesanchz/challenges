class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0

        # l inclusive, r exclusive
        # one element cant be repeated
        l, r = 0, 1

        chars = set(s[0])
        length = 1
        while r < n:
            if s[r] not in chars:
                chars.add(s[r])
                length = max(length, r-l+1)
                r += 1
            else:
                chars.remove(s[l])
                l += 1
        
        return length

