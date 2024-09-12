class Solution:
    def intToRoman(self, num: int) -> str:
        rem = num
        s = str(rem)
        roman = ""

        while rem != 0:
            if s[0] != '4' and s[0] != '9':
                if rem >= 1000:
                    roman += 'M'
                    rem -= 1000
                    s = str(rem)
                elif rem >= 500:
                    roman += 'D'
                    rem -= 500
                    s = str(rem)
                elif rem >= 100:
                    roman += 'C'
                    rem -= 100
                    s = str(rem)
                elif rem >= 50:
                    roman += 'L'
                    rem -= 50
                    s = str(rem)
                elif rem >= 10:
                    roman += 'X'
                    rem -= 10
                    s = str(rem)
                elif rem >= 5:
                    roman += 'V'
                    rem -= 5
                    s = str(rem)
                elif rem >= 1:
                    roman += 'I'
                    rem -= 1
                    s = str(rem)
            else:
                if rem >= 900:
                    roman += 'C'
                    rem += 100
                    s = str(rem)
                elif rem >= 400:
                    roman += 'C'
                    rem += 100
                    s = str(rem)
                elif rem >= 90:
                    roman += 'X'
                    rem += 10
                    s = str(rem)
                elif rem >= 40:
                    roman += 'X'
                    rem += 10
                    s = str(rem)
                elif rem >= 9:
                    roman += 'I'
                    rem += 1
                    s = str(rem)
                elif rem >= 4:
                    roman += 'I'
                    rem += 1
                    s = str(rem)
        
        return roman
