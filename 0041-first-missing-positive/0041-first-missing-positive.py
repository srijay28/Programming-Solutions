class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        s = set(nums)
        x = len(nums)
        for i in range(x):
            if i+1 not in s:
                return i+1
        return x+1
        