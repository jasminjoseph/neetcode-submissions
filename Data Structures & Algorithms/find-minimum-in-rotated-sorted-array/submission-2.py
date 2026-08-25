class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Solution is O(n) but this can be optimised wiht binary search
        #minValue = nums[0]
        #for i in nums:
        #    minValue = min(minValue, i)
        #return minValue

        L = 0 
        R = len(nums) - 1
        ans = nums[0]

        while L <= R:
            mid = L + (R - L) // 2

            if nums[mid] < nums[R]:
                ans = min(ans, nums[mid])
                R = mid - 1
            else:
                ans = min(ans, nums[R])
                L = mid + 1
        return ans