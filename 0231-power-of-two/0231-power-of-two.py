class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False

        x = math.log(n,2)
        
        y = math.pow(2,int(x))
        if y == n:
            return True
        return False