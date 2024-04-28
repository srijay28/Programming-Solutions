class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        m = -float("infinity")
        i = j = 0
        s = 0
        while (j < len(nums) and i <= j):
            s += nums[j]
            if (j - i == k - 1):
                m = max(m,s)
                s -= nums[i]
                i += 1
            j += 1
        return m/k
        