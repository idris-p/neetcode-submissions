class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        result = False

        def explore(row, column, path, visited):
            nonlocal result

            if path == word:
                result = True
                return
            if path[-1] != word[len(path) - 1]:
                return

            nextPos = boardPosition(row, column + 1)
            if not result and column + 1 < len(board[0]) and nextPos not in visited:
                visited.add(nextPos)
                explore(row, column + 1, path + board[row][column + 1], visited)
                visited.remove(nextPos)

            nextPos = boardPosition(row + 1, column)
            if not result and row + 1 < len(board) and nextPos not in visited:
                visited.add(nextPos)
                explore(row + 1, column, path + board[row + 1][column], visited)
                visited.remove(nextPos)

            nextPos = boardPosition(row, column - 1)
            if not result and column > 0 and nextPos not in visited:
                visited.add(nextPos)
                explore(row, column - 1, path + board[row][column - 1], visited)
                visited.remove(nextPos)

            nextPos = boardPosition(row - 1, column)
            if not result and row > 0 and nextPos not in visited:
                visited.add(nextPos)
                explore(row - 1, column, path + board[row - 1][column], visited)
                visited.remove(nextPos)

        def boardPosition(row, column):
            return 10 * row + column

        for row, letters in enumerate(board):
            for column, letter in enumerate(letters):
                if letter == word[0]:
                    explore(row, column, letter, {boardPosition(row, column)})
                    if result:
                        return True

        return False