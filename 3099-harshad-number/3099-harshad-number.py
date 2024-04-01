class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        l = [*str(x)]
        l = [int(i) for i in l]
        s = sum(l)
        if x%s == 0:
            return s
        else:
            return -1
        