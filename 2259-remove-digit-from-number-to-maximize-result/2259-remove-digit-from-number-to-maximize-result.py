class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        res = 0
        flag = False
        for i in range(len(number)):
            if number[i] == digit:
                flag = True
                temp = list(number)
                temp.pop(i)
                res = max(res,int(''.join(temp)))
        if not flag:
            return number
        return str(res)
        