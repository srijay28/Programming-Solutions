class Solution:
    def maximumSwap(self, num: int) -> int:
        s = list(str(num))
        x = y = 0
        m = len(s) - 1
        #finds the max digit on the right(y) and the least digit on the left(x)
        for i in range(m,-1,-1):
            if int(s[i]) > int(s[m]):
                m = i
            elif int(s[i]) < int(s[m]):
                x , y = i , m
        
        s[x] , s[y] = s[y] , s[x]
        return int("".join(s))
    