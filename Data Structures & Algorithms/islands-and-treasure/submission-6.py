class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        visited = set()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    queue.append((i, j))

        count = 0
        while queue:
            for i in range(len(queue)):
                curRow, curCol = queue.popleft()

                if curRow < 0 or curCol < 0 or curRow >= len(grid) or curCol >= len(grid[0]):
                    continue
                if grid[curRow][curCol] == -1:
                    continue
                if (curRow, curCol) in visited:
                    continue 
                visited.add((curRow, curCol))

                grid[curRow][curCol] = count
                
                queue.append((curRow - 1, curCol))
                queue.append((curRow + 1, curCol))
                queue.append((curRow, curCol - 1))
                queue.append((curRow, curCol + 1))

            count += 1