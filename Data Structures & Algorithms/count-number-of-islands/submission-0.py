class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        count = 0

        def visit(i, j):
            if grid[i][j] == "1" and (i, j) not in visited:
                visited.add((i, j))
                if i < len(grid) - 1:
                    visit(i + 1, j)
                if j < len(grid[0]) - 1:
                    visit(i, j + 1)
                if i > 0:
                    visit(i - 1, j)
                if j > 0:
                    visit(i, j - 1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i, j) not in visited:
                    count += 1
                visit(i, j)

        return count