class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        col = []
        pos_diag = []
        neg_diag = []

        all_sol = []
        sol_idx = [] # record queen positions for each row

        def backtrack(r):
            for c in range(n):
                if c in col or (c - r) in pos_diag or (c + r) in neg_diag:
                    continue
                else:
                    sol_idx.append(c)
                    if len(sol_idx) == n:
                        # print(f'queen idx: {sol_idx}')
                        all_sol.append(sol_idx.copy())
                        
                    # record occupied position
                    col.append(c)
                    pos_diag.append(c-r)
                    neg_diag.append(c+r)

                    # print(f'occupied cols: {col}')
                    # print(f'pos_diag: {pos_diag}')
                    # print(f'neg_diag: {neg_diag}')
                    # move to next row, first col
                    backtrack(r + 1)

                    # remove last records then move to next c
                    # for next possible solution
                    sol_idx.pop()
                    # print(f'all sol: {all_sol}')
                    col.pop()
                    pos_diag.pop()
                    neg_diag.pop()

                
            # return row_idx # result of queen positions

        backtrack(0)
        print(all_sol)
        all_res = []
        for sol in all_sol:
            res = []
            for idx in sol:
                row_res = ''
                for i in range(n):
                    if i != idx:
                        row_res += '.'
                    else:
                        row_res += 'Q'
                res.append(row_res)
            all_res.append(res)
        return all_res

                    