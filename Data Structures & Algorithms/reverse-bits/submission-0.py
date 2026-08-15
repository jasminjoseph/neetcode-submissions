class Solution:
    def reverseBits(self, n: int) -> int:
        newNum = 0o00000000000000000000000000000000
        for i in range(32):
            digit = n & 1
            newNum = newNum | (digit << (31 - i))
            n = n >> 1
            print(digit, "and", newNum)
        print(newNum)
        return newNum