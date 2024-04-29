class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        temp = []
        def backt(i,temp):
            if len(temp) == k:
                res.append(temp.copy())
                return
            if i > n:
                return
            for x in range(i,n+1):
                temp.append(x)
                backt(x+1,temp)
                temp.pop()
            
        backt(1,temp)
        return res
            
        