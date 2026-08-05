class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        if not strs:
            return ""
        else:
            for i in strs:
                out += str(len(i))
                out += "#"
                out += i

        return out
        

    def decode(self, s: str) -> List[str]:
        out = []
        if not s:
            return []
        else:
            i = 0
            while i < len(s):
                j = i
                sz = ""

                while s[j] != "#":
                    sz += s[j]
                    j += 1
                i = j
                out.append(s[i+1:i+1+int(sz)])
                i += int(sz) + 1
                
        return out