board = [["5","3",".",".","7",".",".",".","."],
          ["6",".",".","1","9","5",".",".","."],
          [".","9","8",".",".",".",".","6","."],
          ["8",".",".",".","6",".",".",".","3"],
          ["4",".",".","8",".","3",".",".","1"],
          ["7",".",".",".","2",".",".",".","6"],
          [".","6",".",".",".",".","2","8","."],
          [".",".",".","4","1","9",".",".","5"],
          [".",".",".",".","8",".",".","7","9"]]

class Solution:
    def isValidSudoku(self, board) -> bool:
        check = ["1","2","3","4","5","6","7","8","9"]

        cols = len(board)
        rows = len(board[0])

        # --- 1️⃣ Check all rows ---
        for i in range(rows):
            visited = []
            for j in range(cols):
                if board[i][j] in check:
                    if board[i][j] in visited:
                        return False
                    else:
                        visited.append(board[i][j])

        # --- 2️⃣ Check all columns ---
        for i in range(rows):
            visist = []
            for j in range(cols):
                if board[j][i] in check:
                    if board[j][i] in visist:
                       return False
                    else:
                        visist.append(board[j][i])

        # --- 3️⃣ Check all 3x3 boxes ---
        for box_row in range(0, 9, 3):      
            for box_col in range(0, 9, 3):  
                visited = []
                for r in range(box_row, box_row + 3):
                    for c in range(box_col, box_col + 3):
                        if board[r][c] in check:
                            if board[r][c] in visited:
                               return False
                            visited.append(board[r][c])

        return True
