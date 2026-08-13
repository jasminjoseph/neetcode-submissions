class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        gind = 0
        sind = 0
        count = 0

        while gind < len(g) and sind < len(s):
            if g[gind] <= s[sind]:
                count += 1
                gind += 1
                sind += 1
            else:
                sind += 1

        return count

