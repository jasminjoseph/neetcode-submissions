class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for ind, val in enumerate(nums):
            secPart = 0 - val
            L, R = ind + 1, len(nums) - 1

            if ind > 0 and val == nums[ind - 1]:
                continue


            while L < R:
                tempSum = nums[L] + nums[R]
                if tempSum == secPart:
                    result.append([val, nums[L], nums[R]])
                    L += 1
                    while nums[L] == nums[L-1] and L < R :
                        L += 1
                elif tempSum < secPart:
                    L += 1
                else:
                    R -= 1

            
        
        return result

