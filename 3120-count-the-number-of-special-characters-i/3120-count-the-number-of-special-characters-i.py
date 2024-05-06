class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        s = set()
        d = defaultdict(int)
        cnt = 0
        for i in word:
            if 65 <= ord(i) <= 90:
                if (ord(i) + 32) in s:
                    d[i.lower()] += 1
                else:
                    s.add(ord(i)) 
            else:
                if (ord(i)-32) in s:
                    d[i.lower()] += 1
                else:
                    s.add(ord(i))
        return len(d)

   
