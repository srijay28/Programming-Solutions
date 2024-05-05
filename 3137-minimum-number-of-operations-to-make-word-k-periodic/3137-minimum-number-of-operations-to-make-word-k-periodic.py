class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        d = defaultdict(int)
        
        for i in range(0,len(word),k):
            d[word[i:i+k]] += 1
        
        return len(word)//k - max(d.values())