class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1

        # target completely out of bounds
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False

        # find correct 1D array 
        while l <= r:
            m = (l + r) // 2
            if matrix[m][0] <= target <= matrix[m][-1]:
                break
            if target < matrix[m][0]:
                r = m - 1
            else:
                l = m + 1

        # m is correct 1D array
        # normal binary search
        row = matrix[m]
        l, r = 0, len(row) - 1
        
        while l <= r:
            m = (l + r) // 2
            if target == row[m]:
                return True
            if target < row[m]:
                r = m - 1
            else:
                l = m + 1
        return False

        
        

        
        
