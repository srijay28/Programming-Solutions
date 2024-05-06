class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        s = sum(nums)
        diff = abs(s - goal)
        elements = 0
        
        if diff % limit == 0:
            return diff//limit
        else:
            return diff//limit + 1