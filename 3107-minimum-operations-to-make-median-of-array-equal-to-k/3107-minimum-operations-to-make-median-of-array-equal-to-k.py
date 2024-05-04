class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = len(nums)//2
        ops = 0
        
        if nums[i] == k:
            return 0
        elif nums[i] < k:
            while (i < len(nums) and nums[i] < k):
                ops += abs(nums[i] - k)
                i += 1
        elif nums[i] > k: #k is lesser, so reduce nums[i] and thus the numbers preceeding it
            while(i >= 0 and nums[i] > k):
                ops += abs(nums[i] - k)
                i -= 1
        return ops