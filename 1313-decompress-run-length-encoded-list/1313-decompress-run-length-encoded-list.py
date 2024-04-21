class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res = []
        freq = val = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                freq = nums[i]
            else:
                for _ in range(freq):
                    res.append(nums[i])
        return res