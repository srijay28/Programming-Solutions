class Solution:
    def compress(self, chars: List[str]) -> int:
        i = j = 0
        cnt = 0
        ind = 0
        s = ""
        while (i < len(chars)):
            while j < len(chars) and chars[i] == chars[j]:
                cnt += 1
                j += 1
            if cnt == 1:
                chars[ind] = chars[i]
                ind += 1
            else:
                chars[ind] = chars[i]
                ind += 1
                if cnt < 10:
                    chars[ind] = str(cnt)
                    ind += 1
                else:
                    for i in str(cnt):
                        chars[ind] = i
                        ind += 1

            i = j
            j = i
            cnt = 0
        while (len(chars)> ind):
            chars.pop()
        return len(chars)

        