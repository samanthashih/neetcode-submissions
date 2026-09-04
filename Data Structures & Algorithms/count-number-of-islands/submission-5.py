class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # traverse graph 
        # if we find a 1 -> found an island -> bfs to explore all island

        numIslands = 0
        queue = deque()
        seen = set()

        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) in seen:
                    continue

                cell = grid[i][j]
                
                if cell == '1':
                    # bfs on cell
                    numIslands += 1
                    queue.append((i,j))
                    seen.add((i,j))

                    while queue:
                        (x,y) = queue.popleft()
                        # explore neighbors -> if '1' add queue
                        for (a,b) in directions:
                            neighbor = (x+a, y+b)
                            if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and (neighbor[0], neighbor[1]) not in seen:
                                if grid[neighbor[0]][neighbor[1]] == '1':
                                    queue.append(neighbor)
                                    seen.add(neighbor)
                                else:
                                    seen.add(neighbor)
                else:
                    seen.add((i,j))
        
        return numIslands
