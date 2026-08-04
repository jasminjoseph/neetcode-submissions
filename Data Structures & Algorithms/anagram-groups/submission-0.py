class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedMap = defaultdict(list)

        for word in strs:
            sortWord = "".join(sorted(word))
            sortedMap[sortWord].append(word)

        result = []
        for words in sortedMap.values():
            result.append(words)

        return result