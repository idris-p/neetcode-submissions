class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()

        def visit(row, column):
            if grid[row][column] == 1 and (row, column) not in visited:
                visited.add((row, column))
                area = 1

                if row < len(grid) - 1:
                    area += visit(row + 1, column)
                if column < len(grid[0]) - 1:
                    area += visit(row, column + 1)
                if row > 0:
                    area += visit(row - 1, column)
                if column > 0:
                    area += visit(row, column - 1)

                return area
            else:
                return 0

        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited:
                    result = max(visit(i, j), result)

        return result
