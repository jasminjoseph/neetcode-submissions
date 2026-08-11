class Solution:
    def findMin(self, nums: List[int]) -> int:
        minValue = nums[0]

        for i in nums:
            minValue = min(minValue, i)
        return minValue