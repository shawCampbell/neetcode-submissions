class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        l = 0
        r = len(matrix)*len(matrix[0]) - 1
        
        def v_map(n):
            nonlocal matrix
            x = n%len(matrix[0])
            y = n//len(matrix[0])

            return matrix[y][x]

        while l <= r:

            m = l + (r - l)//2


            if (v_map(m) < target):
                l = m+1
            elif (v_map(m) > target):
                r = m-1
            else:
                return True

        return False

        

        
