class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        temp = []
        maxindex = len(nums)
        def bact(i):
            if i >= maxindex:
                res.append(temp.copy())
                return
            temp.append(nums[i])
            bact(i+1)

            #figured it on my own until here, except the .copy()
            temp.pop()
            bact(i+1)

        bact(0)
        return res
        