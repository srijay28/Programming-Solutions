class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #using the numbers in the array as pointers and modifying the variables
        #pointed to by the pointers.
        for i in nums:
            id = abs(i)
            if nums[id] < 0:
                return id
            nums[id] = -nums[id]
        
        