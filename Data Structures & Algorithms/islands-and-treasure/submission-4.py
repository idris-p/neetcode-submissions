from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        def bfs(row, column):
            queue = deque([(row, column)])
            distances = deque([0])
            result = 0
            visited = set()

            while queue:
                curRow, curCol = queue.popleft()
                distance = distances.popleft()

                if (curRow, curCol) in visited:
                    continue 

                if grid[curRow][curCol] == 0:
                    result = distance
                    break
                elif grid[curRow][curCol] == -1:
                    continue

                visited.add((curRow, curCol))
                
                if curRow < len(grid) - 1:
                    queue.append((curRow + 1, curCol))
                    distances.append(distance + 1)
                if curCol < len(grid[0]) - 1:
                    queue.append((curRow, curCol + 1))
                    distances.append(distance + 1)
                if curRow > 0:
                    queue.append((curRow - 1, curCol))
                    distances.append(distance + 1)
                if curCol > 0:
                    queue.append((curRow, curCol - 1))
                    distances.append(distance + 1)

            return result

        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 0:
                    grid[i][j] = bfs(i, j)