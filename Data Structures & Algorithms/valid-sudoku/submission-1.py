class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_sets=[set() for _ in range(9)]
        col_sets=[set() for _ in range(9)]
        box_sets=[[set() for _ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):

                val = board[i][j] 

                if val == '.':
                    continue

                if val in row_sets[i]:
                    return False
                else:
                    row_sets[i].add(val)


                if val in col_sets[j]:
                    return False
                else:
                    col_sets[j].add(val)


                if val in box_sets[i//3][j//3]:
                    return False
                else:
                    box_sets[i//3][j//3].add(val)

        return True

                
