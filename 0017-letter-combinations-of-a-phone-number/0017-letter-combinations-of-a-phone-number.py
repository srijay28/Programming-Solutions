class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # META Question
       
        if not digits: return []
        res = ['']
        var = ''
        for i in digits:
            temp = []
            if int(i) <= 7:
                c = 97 + (int(i)-2)*3
            elif int(i) == 8:
                c = 116
            elif int(i) == 9:
                c = 119
            for x in range(len(res)):
                cnt = 0
                y = c
                while cnt < 4:
                    var = res[x]
                    var += chr(y)
                    cnt += 1
                    temp.append(var)
                    y += 1
                    if cnt == 3 and (c != 112 and c != 119):
                        break
                
            res = temp
        return res



            
        