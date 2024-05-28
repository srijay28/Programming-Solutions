class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        area = 0
        l,r = 0,len(height)-1
        lm = height[l] #leftMax
        rm = height[r] #rightMax

        while (l<r):
            if lm < rm: #leftMax is the bottle-neck
                l += 1
                lm = max(lm,height[l])
                area += lm - height[l]
            else:
                r -= 1 #rightMax is the bottle-neck
                rm = max(rm,height[r])
                area += rm - height[r]
        return area