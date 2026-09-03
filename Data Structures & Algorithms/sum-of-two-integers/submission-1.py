class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        result = 0
        carry = 0

        for i in range(32):
            abit = (a >> i) & 1
            bbit = (b >> i) & 1

            add = abit ^ bbit ^ carry
            carry = (abit + bbit + carry) >= 2
            result = result | add << i

        # Take care of negative numbers
        if result > 0x7FFFFFFF:
            result = ~(result ^ mask) 

        return result