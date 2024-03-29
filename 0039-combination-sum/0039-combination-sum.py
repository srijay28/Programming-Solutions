class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        k = target
        res = []
        temp = []
        def bac(i,s):
            if s == k:
                res.append(temp.copy())
                return
            if s > k or i >= len(candidates):
                return
            
            temp.append(candidates[i])
            bac(i,s+candidates[i])
            temp.pop()

            bac(i+1,s)
        bac(0,0)
        return res

        
        