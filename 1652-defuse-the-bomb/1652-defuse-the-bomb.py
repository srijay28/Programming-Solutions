class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        length = len(code)
        code.extend(code.copy())
        res = []
        s = 0
        if k == 0:
            return [0 for i in range(length)]
        elif k > 0:
            i = j = 0
            while (i < length):
                while j - i <= k:
                    s += code[j]
                    j += 1
                s -= code[i]
                res.append(s)
                i += 1
        
        elif k < 0:
            i = j = length + k
            print(code[i],code[j])
            while (i < 2*length):
                while i - j < -k:
                    s += code[i]
                    i += 1
                if len(res) < length: res.append(s)
                s -= code[j]
                j += 1
        return res
