class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCount = defaultdict(int)

        for i in s:
            sCount[i] += 1

        for j in t:
            sCount[j] -= 1
        
        for c in sCount.values():
            if c != 0:
                return False
        return True

