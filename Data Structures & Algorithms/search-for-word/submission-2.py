class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        global res
        res = False
        def dfs(x, y, word_ptr, d):
            global res
            if word_ptr >= len(word) or x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or (x,y) in d:
                return 

            if board[x][y] == word[word_ptr]:
                d.add((x,y))
                if word_ptr == len(word) - 1:
                    print("word found")
                    res = True
                dfs(x + 1, y, word_ptr + 1, d) or \
                dfs(x, y + 1, word_ptr + 1, d) or \
                dfs(x - 1, y, word_ptr + 1, d) or \
                dfs(x, y - 1, word_ptr + 1, d)
                d.remove((x, y))
            else:
                return 

        for x in range(len(board)):
            for y in range(len(board[0])):
                dfs(x, y, 0, set())

        return res
            



