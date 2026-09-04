class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[r])):
                cell = board[r][c]
                if cell != ".":
                    if cell not in rows[r]:
                        rows[r].add(cell)
                    else:
                        return False

                    if cell not in cols[c]:
                        cols[c].add(cell)
                    else:
                        return False
                    
                    squareNum = (r // 3, c // 3)
                    print("squareNum: ", squareNum)
                    if cell not in squares[squareNum]:
                        squares[squareNum].add(cell)
                    else:
                        return False
        return True
    

                