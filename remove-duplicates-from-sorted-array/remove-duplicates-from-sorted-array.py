class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s = set()
        length = len(nums)
        i = 0
        while (i<length):
            if nums[i] == '-':
                break
            if nums[i] in s:
                nums.pop(i)
                nums.append('-')
                continue
            else:
                s.add(nums[i])
                i += 1
        return i
                