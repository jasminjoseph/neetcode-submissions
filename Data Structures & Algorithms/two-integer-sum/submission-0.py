class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        secondNum = {}

        for ind, val in enumerate(nums):
            second = target - val

            if second in secondNum:
                return [secondNum[second],ind]
            else:
                secondNum[val] = ind

            