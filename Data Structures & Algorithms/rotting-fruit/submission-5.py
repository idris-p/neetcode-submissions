class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        visited = set()
        fresh = set()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh.add((i, j))

        minutes = -1
        while queue:
            for i in range(len(queue)):
                curRow, curCol = queue.popleft()

                if curRow < 0 or curCol < 0 or curRow >= len(grid) or curCol >= len(grid[0]):
                    continue
                if grid[curRow][curCol] == 0:
                    continue
                if (curRow, curCol) in visited:
                    continue
                visited.add((curRow, curCol))

                grid[curRow][curCol] = 2

                queue.append((curRow + 1, curCol))
                queue.append((curRow - 1, curCol))
                queue.append((curRow, curCol + 1))
                queue.append((curRow, curCol - 1))
            minutes += 1

        for fruit in fresh:
            if fruit not in visited:
                return -1

        result = minutes - 1
        return result if result > 0 else 0
