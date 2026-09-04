class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        to_visit = [] # stack
        visited = set()

        rows = len(grid)
        cols = len(grid[0])

        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == '1' and (x,y) not in visited:
                    to_visit.append((x,y))
                    islands += 1

                while len(to_visit) != 0:
                    x, y = to_visit.pop()
                    visited.add((x,y))

                    # up
                    if 0 <= x < rows and 0 <= y+1 < cols and grid[x][y+1] == '1' and (x,y+1) not in visited:
                        to_visit.append((x,y+1))
                    # down
                    if 0 <= x < rows and 0 <= y-1 < cols and grid[x][y-1] == '1' and (x,y-1) not in visited:
                        to_visit.append((x,y-1))
                    # left
                    if 0 <= x-1 < rows and 0 <= y < cols and grid[x-1][y] == '1' and (x-1,y) not in visited:
                        to_visit.append((x-1,y))
                    # right
                    if 0 <= x+1 < rows and 0 <= y < cols and grid[x+1][y] == '1' and (x+1,y) not in visited:
                        to_visit.append((x+1,y))
        return islands

    