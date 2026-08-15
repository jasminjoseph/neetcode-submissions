class Solution:
    def hammingWeight(self, n: int) -> int:
        ret = 0
        for i in range(32):
            digit = n & 1
            if digit == 1:
                ret += 1
            n = n >> 1

        return ret