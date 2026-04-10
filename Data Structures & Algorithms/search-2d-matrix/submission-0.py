class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # pointer to search first integer of each row first
        out_start_ptr = 0
        out_end_ptr = len(matrix) - 1
        # find row to search - 
        # target falls between first integers of curr and next row
        while out_start_ptr <= out_end_ptr:
            outer_ptr = (out_start_ptr + out_end_ptr) // 2
            row = matrix[outer_ptr]
            if target >= row[0] and target <= row[-1]:
                start_ptr = 0
                end_ptr = len(row) - 1
                while start_ptr <= end_ptr:
                    inner_ptr = (start_ptr + end_ptr) // 2
                    value = row[inner_ptr]
                    print(start_ptr)
                    print(end_ptr)
                    if target == value:
                        return True
                    elif target > value:
                        start_ptr = inner_ptr + 1
                    else:
                        end_ptr = inner_ptr - 1
                return False
            elif target < row[0]:
                out_end_ptr = outer_ptr - 1
            
            else:
                out_start_ptr = outer_ptr + 1
        return False
                         