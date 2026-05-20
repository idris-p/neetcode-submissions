class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        maximum = 0
        visited = set()
        def dfs(row, column):
            if row < 0 or row >= len(grid) or column < 0 or column >= len(grid[0]):
                return 0
            if grid[row][column] == 0:
                return 0
            if (row, column) in visited:
                return 0

            visited.add((row, column))

            size = 1

            size += dfs(row + 1, column)
            size += dfs(row - 1, column)
            size += dfs(row, column + 1)
            size += dfs(row, column - 1)

            return size

        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                val = dfs(i, j)
                maximum = max(val, maximum)

        return maximum