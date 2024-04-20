class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        s = self.countAndSay(n-1)
        i = j = 0
        cnt = 0
        res = ""
        while (i < len(s)):
            while j < len(s) and (s[i] == s[j]):
                cnt += 1
                j += 1
            else:
                res += str(cnt) + s[i]
                i = j
                j = i
                cnt = 0
                continue
        return res