class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        for i in ops:
            if i == "C":
                stack.pop()
            elif i == "D":
                x = stack[-1]
                stack.append(2*x)
            elif i == '+':
                x = stack.pop()
                y = stack.pop()
                stack.append(y)
                stack.append(x)
                stack.append(x+y)
            else: 
                stack.append(int(i))
        return sum(stack)
        