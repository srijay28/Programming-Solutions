class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        cnt = res = 0
        length = len(word)
        i = 0
        while i < len(sequence):
            if sequence[i:i+length] == word:
                while sequence[i:i+length] == word:
                    print(i,sequence[i:i+length])
                    cnt += 1
                    i += length
                res = max(res,cnt)
                cnt = 0
                i -= length - 1
                continue
            i += 1
        return res

        