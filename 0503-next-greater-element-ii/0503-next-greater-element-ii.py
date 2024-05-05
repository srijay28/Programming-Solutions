class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        def val():
            return -1
        nums.extend(nums.copy())
        d = defaultdict(val)
        stack = []
        for i,n in enumerate(nums):
            if not stack:
                stack.append((i,n))
            else:
                while stack and stack[-1][1] < n:
                    d[stack.pop()[0]] = n
                stack.append((i,n))
        return [d[i] for i in range(len(nums)//2)]
        