class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        visited = set()

        def dfs(row, column, ocean):
            if row < 0 or column < 0 or row >= len(heights) or column >= len(heights[0]):
                return
            if (row, column) in visited:
                return

            visited.add((row, column))
            ocean.add((row, column))

            if row > 0 and heights[row][column] <= heights[row - 1][column]:
                dfs(row - 1, column, ocean)
            if row < len(heights) - 1 and heights[row][column] <= heights[row + 1][column]:
                dfs(row + 1, column, ocean)
            if column > 0 and heights[row][column] <= heights[row][column - 1]:
                dfs(row, column - 1, ocean)
            if column < len(heights[0]) - 1 and heights[row][column] <= heights[row][column + 1]:
                dfs(row, column + 1, ocean)

        for i in range(len(heights[0])):
            dfs(0, i, pacific)
        for i in range(len(heights)):
            dfs(i, 0, pacific)
        visited = set()
        for i in range(len(heights[0])):
            dfs(len(heights) - 1, i, atlantic)
        for i in range(len(heights)):
            dfs(i, len(heights[0]) - 1, atlantic)

        result = []
        for (row, column) in pacific:
            if (row, column) in atlantic:
                result.append([row, column])

        return result