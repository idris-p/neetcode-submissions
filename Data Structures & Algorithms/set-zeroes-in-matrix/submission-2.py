class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = set()
        cols = set()

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    rows.add(r)
                    cols.add(c)

        for row in rows:
            matrix[row] = [0] * len(matrix[0])

        for col in cols:
            for i in range(len(matrix)):
                matrix[i][col] = 0