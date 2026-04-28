class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in board:
            s = set()
            for i in row:
                if i == ".":
                    continue
                if i in s:
                    return False
                s.add(i)

        sub = set()
        for i in range(len(board[0])):
            s = set()
            for j in range(len(board)):
                if board[j][i] == ".":
                    continue
                if board[j][i] in s:
                    return False
                s.add(board[j][i])
                tup = (board[j][i], j // 3, i // 3)
                if tup in sub:
                    return False
                sub.add(tup)
        
        return True

