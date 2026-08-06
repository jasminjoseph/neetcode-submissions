class Solution:
    def isValid(self, s: str) -> bool:
        myStack = []
        paraMap = {"}":"{", "]":"[", ")":"("}

        for i in s:
            if i not in paraMap:
                myStack.append(i)
            else:
                if myStack == []:
                    return False
                pop = myStack.pop()
                if pop != paraMap[i]:
                    return False
        if myStack == []:
            return True
        else:
            return False




                