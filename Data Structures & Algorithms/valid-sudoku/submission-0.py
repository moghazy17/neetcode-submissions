class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_sets=[set() for _ in range(9)]
        col_sets=[set() for _ in range(9)]
        box_sets=[[set() for _ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):

                if board[i][j] == '.':
                    continue

                if board[i][j] in row_sets[i]:
                    return False
                else:
                    row_sets[i].add(board[i][j])


                if board[i][j] in col_sets[j]:
                    return False
                else:
                    col_sets[j].add(board[i][j])


                if board[i][j] in box_sets[i//3][j//3]:
                    return False
                else:
                    box_sets[i//3][j//3].add(board[i][j])

        return True

                
