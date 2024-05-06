class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        s = set()
        res = set()
        d = defaultdict(int)
        for i in word:
            if i.islower():
                if d[i.upper()] > 0:
                    res.discard(i.upper())
                    s.discard(i)
                else:
                    s.add(i)
            else:
                d[i] += 1
                if i.lower() in s:
                    res.add(i)

        return len(res)