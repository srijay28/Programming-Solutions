class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0 or k == 1: return 0
        i = j = cnt = 0
        prod = 1
        while j < len(nums):
            prod*=nums[j]
            while prod >= k:
                prod /= nums[i]
                i += 1
            cnt += 1 + (j - i)
            j += 1
        return cnt
        