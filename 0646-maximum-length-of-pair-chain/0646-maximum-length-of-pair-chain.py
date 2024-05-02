class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key = lambda x:x[1])
        length = 1
        prev = pairs[0][1]
        i = 0
        while (i < len(pairs)):
            if prev < pairs[i][0]:
                length += 1
                prev = pairs[i][1]
            i += 1
        return length