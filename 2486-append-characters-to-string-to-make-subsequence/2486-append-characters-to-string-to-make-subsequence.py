class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = j = 0
        m , n = len(s) , len(t)
        cnt = 0
        while (i < m) and (j < n):
            if s[i] == t[j]:
                cnt += 1
                j += 1
            i += 1
        return n - cnt
