class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        s = set(nums)
        maxi = -1
        for i in nums:
            if -i in s:
                maxi = max(maxi,abs(i))
        return maxi

        