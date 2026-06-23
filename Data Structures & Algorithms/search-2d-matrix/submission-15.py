class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) * len(matrix[0])

        while left < right:
            middle = left + (right - left) // 2
            r = middle // len(matrix[0])
            c = middle % len(matrix[0])

            if target == matrix[r][c]:
                return True
            elif target < matrix[r][c]:
                right = middle
            else:
                left = middle + 1

        return False