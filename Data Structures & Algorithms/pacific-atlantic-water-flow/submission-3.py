class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        result = []      

        def bfs(row, column):
            pacific = False
            atlantic = False
            queue = deque([(row, column)])
            visited = set()

            while queue:
                curRow, curCol = queue.popleft()

                if (curRow, curCol) in visited:
                    continue

                visited.add((curRow, curCol))
                visited.add((curRow, curCol))

                if curRow == 0 or curCol == 0:
                    pacific = True
                if curRow == len(heights) - 1 or curCol == len(heights[0]) - 1:
                    atlantic = True
                
                if curRow < len(heights) - 1 and heights[curRow + 1][curCol] <= heights[curRow][curCol]:
                    queue.append((curRow + 1, curCol))
                if curCol < len(heights[0]) - 1 and heights[curRow][curCol + 1] <= heights[curRow][curCol]:
                    queue.append((curRow, curCol + 1))
                if curRow > 0 and heights[curRow - 1][curCol] <= heights[curRow][curCol]:
                    queue.append((curRow - 1, curCol))
                if curCol > 0 and heights[curRow][curCol - 1] <= heights[curRow][curCol]:
                    queue.append((curRow, curCol - 1))

            if pacific and atlantic:
                result.append([row, column])

        for i in range(len(heights)):
            for j in range(len(heights[0])):
                bfs(i, j)

        return result