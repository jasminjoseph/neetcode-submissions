class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = len(nums)

        for i in range(total):
            if i not in nums:
                return i
        
        return total