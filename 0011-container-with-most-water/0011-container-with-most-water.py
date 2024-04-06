class Solution:
    def maxArea(self, h: List[int]) -> int:
    #find a pair such that the product of difference between their indices       #and the lesser of the wo should be max 
        area = pro = l = 0
        r = len(h)-1
        while(l<r):
            s=min(h[l],h[r]) #minimum decides the amount
            area=max(area,(r-l)*s)
            if (h[l]<h[r]):
                l+=1
            elif (h[l]>h[r]):
                r-=1
            else:
                l+=1
        return area

        