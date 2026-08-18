class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        n = len(matrix)
        mid = n // 2
        offset = 0
        reverseParity = 1 if n % 2 == 0 else 0

        while mid + offset < n:
            temp = []
            for i in range(mid - offset - reverseParity, mid + offset + 1):
                temp.append(matrix[mid - offset - reverseParity][i])
            
            for i in range(mid - offset - reverseParity, mid + offset + 1):
                matrix[mid - offset - reverseParity][n - 1 - i] = matrix[i][mid - offset - reverseParity]

            for i in range(mid - offset - reverseParity, mid + offset + 1):
                matrix[i][mid - offset - reverseParity] = matrix[mid + offset][i]

            for i in range(mid - offset - reverseParity, mid + offset + 1):
                matrix[mid + offset][i] = matrix[n - 1 - i][mid + offset]

            for i in range(len(temp)):
                matrix[mid - (len(temp) // 2) + i][mid + offset] = temp[i]

            offset += 1