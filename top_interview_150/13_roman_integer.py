class Solution:
    def romanToInt(self, s: str) -> int:
        
        s = list(s)
        n = len(s)
        num = 0

        for i in range(n):
            if s[i] == 'I':
                if i != n-1 and s[i+1] in ['V', 'X']:
                    num -= 1
                else:
                    num += 1
            elif s[i] == 'V':
                num += 5
            elif s[i] == 'X':
                if i != n-1 and s[i+1] in ['L', 'C']:
                    num -= 10
                else:
                    num += 10
            elif s[i] == 'L':
                num += 50
            elif s[i] == 'C':
                if i != n-1 and s[i+1] in ['D', 'M']:
                    num -= 100
                else:
                    num += 100
            elif s[i] == 'D':
                num += 500
            elif s[i] == 'M':
                num += 1000

            else:
                raise Exception("Caso no esperado:", s[i])

        return num
