class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word = False
        counter = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] != ' ':
                counter += 1
                word = True

            if word and s[i] == ' ':
                break

        return counter
