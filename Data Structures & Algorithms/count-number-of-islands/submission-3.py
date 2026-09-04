class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # for cell in grid
            # mark cell as visited
            # if find land, run BFS to find all connected land ('1')
                # count++
        # return count

        visited = set()
        numIslands = 0


        def bfs(x, y):
            # add valid neighbors to queue + mark visited
                # valid -> land ('1') and NOT visited
            # run while queue != empty -> no more connected land neighbors, island done
            directions = [[0,1], [0,-1], [1,0], [-1,0]]
            queue = deque()
            queue.append((x,y))

            while queue:
                currX, currY = queue.popleft()
                for d in directions:
                    neighborX = currX+d[0]
                    neighborY = currY+d[1]
                    if 0 <= neighborX < len(grid) and 0 <= neighborY < len(grid[0]):
                        if grid[neighborX][neighborY] == '1' and (neighborX, neighborY) not in visited:
                            queue.append((neighborX, neighborY))
                        visited.add((neighborX, neighborY))

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if (x,y) not in visited:
                    visited.add((x,y))
                    if grid[x][y] == '1':
                        bfs(x,y)
                        numIslands += 1
                    else:
                        visited.add((x,y))


        return numIslands
                