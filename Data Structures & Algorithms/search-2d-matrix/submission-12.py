class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        ROWS = len(matrix)
        COLS = len(matrix[0])

        l, r = 0, ROWS*COLS - 1

        def n_to_row_col(n):
            col = n%COLS
            row = n//COLS
            return row, col

        while l <= r:
            m = l + (r - l)//2

            row_m, col_m = n_to_row_col(m)
            n_m = matrix[row_m][col_m]

            if n_m < target:
                l = m + 1
            elif n_m > target:
                r = m - 1
            else:
                return True

        return False