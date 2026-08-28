class Solution:
    def countBits(self, n: int) -> List[int]:
        countList = []
        #numB = bin(num)
    

        for i in range(n+1):
            countList.append(self.getOne(i))
        return countList

    def getOne(self, num: int) -> int:
        count = 0
        while num:
            getOne = num & 1
            if getOne == 1:
                count += 1
            num = num >> 1
        return count


