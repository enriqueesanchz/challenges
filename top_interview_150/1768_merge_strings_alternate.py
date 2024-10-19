class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = len(word1)
        m = len(word2)

        mn = min(n, m)

        res = ""
        for i in range(mn):
            res += word1[i] + word2[i]

        res += word1[m:]
        res += word2[n:]
        return res
