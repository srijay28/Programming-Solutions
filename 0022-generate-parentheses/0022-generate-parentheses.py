class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        def backt(openp,closep):
            if openp == closep == n:
                res.append(("").join(stack))
                return
            if openp < n:
                stack.append("(")
                backt(openp + 1, closep)
                stack.pop()  #popping the last element that was added, not the above opening bracket
            if closep < openp:
                stack.append(")")
                backt(openp , closep + 1)
                stack.pop()
        backt(0,0) #calling function
        return res

        