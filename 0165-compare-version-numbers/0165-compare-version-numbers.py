class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        s1 = s2 = 0
        l1 = version1.split('.')
        l2 = version2.split('.')
        cnt = 0
        length1 , length2 = len(l1) , len(l2)
        if length1 > length2:
            while cnt < length1 - length2:
                l2.append('0')
                cnt += 1

        elif length2 > length1:
            while cnt < length2 - length1:
                l1.append('0')
                cnt += 1
        l1 = [int(i) for i in l1]
        l1 = [str(i) for i in l1]
        l2 = [int(i) for i in l2]
        l2 = [str(i) for i in l2]
        
        s1 = int(''.join(l1))
        s2 = int(''.join(l2))

        if s1 > s2:
            return 1
        elif s1 < s2:
            return -1
        else:
            return 0
            