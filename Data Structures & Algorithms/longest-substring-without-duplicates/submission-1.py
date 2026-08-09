from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        ansString = set()
        maxLen = 0

        for elem in range(len(s)):
            if s[elem] not in ansString:
                ansString.add(s[elem])
            else:
                while s[elem] in ansString:
                    ansString.remove(s[L])
                    L += 1
                ansString.add(s[elem])
            maxLen = max(maxLen, len(ansString))
        return maxLen
        
