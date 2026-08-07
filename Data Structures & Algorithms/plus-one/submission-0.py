class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        digits[-1] = digits[-1] + 1
        for i in range(len(digits)-1,-1,-1):
            digits[i] += carry
            if digits[i] > 9:
                carry = 1
                digits[i] = digits[i] - 10
            else:
                carry = 0
        if carry == 1:
            return [1] + digits
        else:
            return digits