class Solution:
    def addBinary(self, a: str, b: str) -> str:
        diff = abs(len(a) - len(b))
        leading = '0' * diff
        if len(a) > len(b):
            b = leading + b
        else:
            a = leading + a
        
        res = ""
        carry = "0"
        for i in range(len(a)-1,-1,-1):
            sum = int(a[i]) + int(b[i]) + int(carry)
            if sum == 0:
                res = "0" + res
                carry = "0"
            elif sum == 1:
                res = "1" + res
                carry = "0"
            elif sum == 2:
                res = "0" + res
                carry = "1"
            else:
                res = "1" + res
                carry = "1"
        
        if carry == "1":
            res = carry + res
        return res