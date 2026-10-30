class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in range(9):
            seen = set()
            for c in range(9):
                if board[r][c] == ".":
                    continue
                elif board[r][c] in seen:
                    return False
                else:
                    seen.add(board[r][c])
        for c in range(9):
            seen = set()
            for r in range(9):
                if board[r][c] == ".":
                    continue
                elif board[r][c] in seen:
                    return False
                else:    
                    seen.add(board[r][c])
        for r in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (r // 3) * 3 + i
                    col = (r % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    elif board[row][col] in seen:
                        return False
                    else:    
                        seen.add(board[row][col])
        return True