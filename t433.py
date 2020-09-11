from queue import Queue
class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        # write your code here
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == -1:
                    res += 1
                    grid[i][j] = 0
                    cur = Queue()
                    cur.put((i, j))
                    while cur.not_empty:
