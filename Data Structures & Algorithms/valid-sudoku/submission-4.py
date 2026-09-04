class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        l = len(board)

        rows = [[False] * 9 for i in range(l)]
        cols = [[False] * 9 for i in range(l)]
        sqrs = [[False] * 9 for i in range(l)]

        for row in range(l):
            for col in range(l):
                num = board[row][col]
                if num != '.':
                    num = int(num) - 1
                    sqr = 3 * (row // 3) + (col // 3)

                    if rows[row][num] or cols[col][num] or sqrs[sqr][num]:
                        return False
                    
                    rows[row][num] = True
                    cols[col][num] = True
                    sqrs[sqr][num] = True

        return True