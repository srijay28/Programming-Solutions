class Solution:
    def isValid(self, word: str) -> bool:
        vowels = {'a','e','i','o','u','A','E','I','O','U'}
        v = False
        c = False
        digits = False
        if len(word) >= 3:
            for i in word:
                if i in vowels:
                    v = True
                    continue
                if i not in vowels and (65<=ord(i)<=90 or 97<=ord(i)<=122):
                    c = True
                    continue
                if 48<=ord(i)<=57:
                    continue
                return False
            return v and c

        else:
            return False
        