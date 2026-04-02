class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkSubBox(x, y):
            numbers = []
            for i in range(x, x+3):
                for j in range(y, y+3):
                    if board[j][i] in numbers:
                        return False
                    else:
                        if board[j][i] != ".":
                            numbers.append(board[j][i])
            return True
        
        def checkRow(y):
            numbers = []
            for i in range(0, 9):
                if board[y][i] in numbers:
                    return False
                else:
                    if board[y][i] != ".":
                        numbers.append(board[y][i])
            return True

        def checkColumn(x):
            numbers = []
            for i in range(0, 9):
                if board[i][x] in numbers:
                    return False
                else:
                    if board[i][x] != ".":
                        numbers.append(board[i][x])
            return True
        
        valid = True
        for i in range(0, 9):
            if not (checkRow(i) and checkColumn(i)):
                valid = False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not checkSubBox(i, j):
                    valid = False

        return valid
        