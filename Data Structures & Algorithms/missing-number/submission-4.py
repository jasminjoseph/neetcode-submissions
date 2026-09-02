class Solution:
    def missingNumber(self, nums: List[int]) -> int:
#        total = len(nums)
#        for i in range(total):
#            if i not in nums:
#                return i       
#        return total

        # Bitwise XOR 
        xorr = len(nums)
        for i in range(xorr):
            xorr = xorr ^ i ^ nums[i]

        return xorr