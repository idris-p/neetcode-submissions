class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkRow(y):
            seen = set()
            for i in range(9):
                num = board[y][i]
                if num in seen:
                    return False
                if num != ".":
                    seen.add(num)
            return True

        def checkColumn(x):
            seen = set()
            for i in range(9):
                num = board[i][x]
                if num in seen:
                    return False
                if num != ".":
                    seen.add(num)
            return True

        def checkSubBox(x, y):
            seen = set()
            for i in range(3):
                for j in range(3):
                    num = board[y + i][x + j]
                    if num in seen:
                        return False
                    if num != ".":
                        seen.add(num)
            return True

        valid = True
        for i in range(9):
            valid = valid and checkRow(i) and checkColumn(i)
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                valid = valid and checkSubBox(i, j)

        return valid