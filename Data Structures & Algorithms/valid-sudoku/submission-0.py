class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        l = len(board)

        rows = [[False]*l for i in range(l)] 
        cols = [[False]*l for i in range(l)] 
        squares = [[False]*l for i in range(l)] 

        for row in range(l):
            for col in range(l):
                if board[row][col] != '.':
                    square = (row//3) * 3 + (col//3)
                    num = ord(board[row][col]) - ord('1')
                    if rows[row][num] or cols[col][num] or squares[square][num]:
                        return False
                    
                    rows[row][num] = cols[col][num] = squares[square][num] = True

        return True