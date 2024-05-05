class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = defaultdict(int)
        stack = []
        res = []
        for i in range(len(nums2)):
            if not stack:
                stack.append(nums2[i])
            else:
                while stack and stack[-1] < nums2[i]:
                    d[stack.pop()] = nums2[i]
                stack.append(nums2[i])
        for i in nums1:
            if d[i] == 0:
                res.append(-1)
                continue
            res.append(d[i])
        return res