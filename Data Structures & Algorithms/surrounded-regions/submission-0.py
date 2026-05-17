class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        surroundedCells = set()
        def isSurrounded(row, column):
            visited = set()
            queue = deque([(row, column)])

            def onEdge(r, c):
                return r == 0 or c == 0 or r == len(board) - 1 or c == len(board[0]) - 1

            while queue:
                curRow, curCol = queue.popleft()

                if (curRow, curCol) in visited:
                    continue

                visited.add((curRow, curCol))

                if onEdge(curRow, curCol):
                    return False

                if board[curRow + 1][curCol] == "O":
                    queue.append((curRow + 1, curCol))
                if board[curRow][curCol + 1] == "O":
                    queue.append((curRow, curCol + 1))
                if board[curRow - 1][curCol] == "O":
                    queue.append((curRow - 1, curCol))
                if board[curRow][curCol - 1] == "O":
                    queue.append((curRow, curCol - 1))

            for cell in visited:
                surroundedCells.add(cell)
            return True

        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i, j) in surroundedCells:
                    board[i][j] = "X"
                elif board[i][j] == "O" and isSurrounded(i, j):
                    board[i][j] = "X"