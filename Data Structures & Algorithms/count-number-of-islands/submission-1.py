class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        visited = set()
        def dfs(row, column):
            if row < 0 or row >= len(grid) or column < 0 or column >= len(grid[0]):
                return 0
            if grid[row][column] == "0":
                return 0
            if (row, column) in visited:
                return 0

            visited.add((row, column))

            dfs(row + 1, column)
            dfs(row - 1, column)
            dfs(row, column + 1)
            dfs(row, column - 1)

            return 1
        
        
        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                count += dfs(i, j)
        
        return count