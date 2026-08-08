class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        visited = []

        # Visit all rows
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] not in visited:
                    visited.append(board[i][j])
                else:
                    return False
            visited = []

        # Visit all columns
        for i in range(9):
            for j in range(9):
                if board[j][i] == ".":
                    continue;
                if board[j][i] not in visited:
                    visited.append(board[j][i])
                else:
                    return False
            visited = []

        # For all 3x3 boxes, total 9 boxes
        for box in range(9):
            for i in range(3):
                for j in range(3):
                    row = (box // 3) * 3 + i
                    col = (box % 3) * 3 + j

                    if board[row][col] == ".":
                        continue
                    if board[row][col] not in visited:
                        visited.append(board[row][col])
                    else:
                        return False
            visited = []

        return True
                