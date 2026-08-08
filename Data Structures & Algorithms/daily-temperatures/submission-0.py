class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for ind, val in enumerate(temperatures):
            while stack and val > stack[-1][0]:
                temp, tempInd = stack.pop()
                result[tempInd] = ind - tempInd
            stack.append([val, ind])

        return result