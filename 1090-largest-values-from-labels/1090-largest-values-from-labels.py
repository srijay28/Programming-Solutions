class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        score = cnt = 0
        pairs = list(zip(values,labels))
        pairs.sort(reverse = True)
        d = defaultdict(int)
        for i in pairs:
            if cnt == numWanted:
                break
            if d[i[1]] >= useLimit:
                continue
            else:
                score += i[0]
                d[i[1]] += 1
                cnt += 1
        return score