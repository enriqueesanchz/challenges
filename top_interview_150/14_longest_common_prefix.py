from typing import List

class Solution:
    def longestCommonPrefix(self, v: List[str]) -> str:
        pref = v[0]
        pref_len = len(pref)

        for i in range(1, len(v)):
            while pref[:pref_len] != v[i][:pref_len]:
                pref_len -= 1
                if pref_len == 0:
                    return ""
        
        return pref[:pref_len]
