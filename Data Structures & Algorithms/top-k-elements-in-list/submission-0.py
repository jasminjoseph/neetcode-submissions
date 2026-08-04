class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        minHeap = []
        countMap = defaultdict(int)

        for i in nums:
            countMap[i] += 1

        for i in countMap:
            heapq.heappush(minHeap, [countMap[i],i])
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        result = []
        for i in minHeap:
            result.append(i[1])
        return result

            

            


