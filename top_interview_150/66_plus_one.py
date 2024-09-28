from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        carry = 1
        i = len(digits) - 1
        while carry != 0:
            if i >= 0:
                sm = digits[i] + carry
                digits[i] = sm % 10
            else:
                sm = carry
                digits.insert(0, sm)
                
            carry = sm // 10
            i -= 1

        return digits
