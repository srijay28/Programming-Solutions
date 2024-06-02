class Solution:
    def reverseVowels(self, s: str) -> str:
        i = 0
        j = len(s) - 1
        v = {'a','e','i','o','u','A','E','I','O','U'}
        s = list(s)
        flagi , flagj = False , False
        while (i<j):
            if s[i] in v:
                flagi = True
            if s[j] in v:
                flagj = True
            if s[i] not in v and not flagi:
                i += 1
            if s[j] not in v and not flagj:
                j -= 1
            if flagi and flagj:
                s[i],s[j] = s[j],s[i]
                flagi = False
                flagj = False
                i += 1
                j -= 1
        return "".join(s)
            
            