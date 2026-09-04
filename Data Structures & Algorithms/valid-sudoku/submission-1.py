class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Store each row, col, square as rows={row1 : set(1,2,3,..9)}
        # Iterate each cell and add to row, col, square sets. 
            # If cell already in a set, return False
        
        rows = defaultdict(set) # i
        cols = defaultdict(set) # j
        squares = defaultdict(set) # floor(i/3), floor(j/3)

        for i in range(9):
            for j in range(9):
                cell = board[i][j]
                if cell == ".":
                    continue

                squareI, squareJ = math.floor(i/3), math.floor(j/3)
                
                if ((cell in rows[i]) or (cell in cols[j]) or (cell in squares[(squareI, squareJ)])):
                    # print("repeat cell: ", cell, " i:", i, " j:", j, " square: ", squareI, squareJ)
                    return False
                else:
                    rows[i].add(cell)
                    cols[j].add(cell)
                    squares[(squareI, squareJ)].add(cell)
                
        return True
