class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = (0, 0), (len(matrix)-1, len(matrix[0])-1)
        
        while (l[0] < r[0]) or (l[0] == r[0] and l[1] <= r[1]):
            mid = ((r[0] - l[0] // 2) + l[0], (r[1] - l[1] // 2) + l[1])

            if target == matrix[mid[0]][mid[1]]:
                return True
            elif target < matrix[mid[0]][mid[1]]:
                r = (mid[0], mid[1] - 1)
                if r[1] < 0:
                    r = (r[0] - 1, len(matrix[0]) - 1)
            elif target > matrix[mid[0]][mid[1]]:
                l = (mid[0], mid[1] + 1)
                if l[1] >= len(matrix[0]):
                    l = (l[0] + 1, 0)

        return False
