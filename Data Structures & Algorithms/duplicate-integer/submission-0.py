class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsCount = defaultdict(int)

        for i in nums:
            numsCount[i] += 1

            if numsCount[i] > 1:
                return True

        return False

        