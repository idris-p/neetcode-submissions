class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        notSurrounded = set()
        def dfs(row, column):
            if row < 0 or column < 0 or row >= len(board) or column >= len(board[0]):
                return
            if board[row][column] == "X":
                return
            if (row, column) in notSurrounded:
                return

            notSurrounded.add((row, column))

            dfs(row + 1, column)
            dfs(row - 1, column)
            dfs(row, column + 1)
            dfs(row, column - 1)

        for i in range(len(board[0])):
            dfs(0, i)
            dfs(len(board) - 1, i)
        for i in range(len(board)):
            dfs(i, 0)
            dfs(i, len(board[0]) - 1)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O" and (i, j) not in notSurrounded:
                    board[i][j] = "X"