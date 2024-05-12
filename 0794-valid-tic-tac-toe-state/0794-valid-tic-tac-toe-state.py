class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        x = o = 0
        jlist = [0 for i in range(3)]
        i_j = j_i = 0
        tempresx = tempreso = 0
        cnt = 0
        for i in range(3):
            tempx = tempo = 0
            for j in range(3):
                if board[i][j] == "X":
                    if i == j:
                        i_j += 1
                    if ((i == 0 and j == 2) or (i == 1 and j == 1) or (i == 2 and j == 0)):
                        j_i += 1
                    x += 1
                    tempx += 1
                    jlist[j] += 1
                elif board[i][j] == "O":
                    if i == j:
                        i_j -= 1
                    if (i==0 and j ==2) or (i==1 and j==1) or (i==2 and j==0):
                        j_i -= 1
                    o += 1
                    tempo += 1
                    jlist[j] -= 1
            tempresx = max(tempresx,tempx)
            tempreso = max(tempreso,tempo)
        for z in jlist:
            if z == 3 or z == -3:
                cnt += 1
        if cnt > 1:
            return False
        print(j_i)
        if tempreso == 3 and tempresx == 3:
            return False
        if tempresx == 3 or i_j == 3 or j_i == 3:
            if x <= o:
                return False
        if tempreso == 3 or i_j == -3 or j_i == -3:
            if not x == o:
                return False
        if x == o or o+1 == x:
            return True
        return False