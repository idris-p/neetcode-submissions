class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        notIsolated = set()
        # Check for isolated fresh fruit
        def isIsolated(row, column):
            queue = deque([(row, column)])
            visited = set()

            def addToQueue(r, c):
                if grid[r][c] != 0 and (r, c) not in visited:
                    queue.append((r, c))

            while queue:
                curRow, curCol = queue.popleft()

                visited.add((curRow, curCol))
                if grid[curRow][curCol] == 2:
                    for fruit in visited:
                        notIsolated.add(fruit)
                    for fruit in queue:
                        notIsolated.add(fruit)
                    return False

                if curRow < len(grid) - 1:
                    addToQueue(curRow + 1, curCol)
                if curCol < len(grid[0]) - 1:
                    addToQueue(curRow, curCol + 1)
                if curRow > 0:
                    addToQueue(curRow - 1, curCol)
                if curCol > 0:
                    addToQueue(curRow, curCol - 1)

            return True

        queue = deque([])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in notIsolated:
                    if isIsolated(i, j):
                        return -1
                elif grid[i][j] == 2:
                    queue.append((i, j))

        # Rot fruit
        result = -1
        while queue:
            for i in range(len(queue)):
                row, column = queue.popleft()

                # Rot neighbours
                def rot(r, c):
                    if grid[r][c] == 1:
                        grid[r][c] = 2
                        queue.append((r, c))

                if row < len(grid) - 1:
                    rot(row + 1, column)
                if column < len(grid[0]) - 1:
                    rot(row, column + 1)
                if row > 0:
                    rot(row - 1, column)
                if column > 0:
                    rot(row, column - 1)

            result += 1

        if result < 0:
            return 0
        return result