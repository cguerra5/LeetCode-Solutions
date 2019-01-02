class Solution:
    def minPathSum(self, grid):
        """
        Finds a path from top left to bottom right which minimizes the sum of 
        all numbers along its path and returns the sum.
        
        :param grid: A grid with an integer cost associated with each point.
        :type grid: List[List[int]]
        :return: The total cost of the minimum cost path.
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        
        row_count = len(grid)
        col_count = len(grid[0])
        
        # Memoizes the minimum cost to each node
        cost = [[0 for _ in grid[0]] for _ in grid]
        cost[0][0] = grid[0][0]
        
        # Since we can only move to the right and downwards, the min cost to
        # any point on the top row is the sum of all point to its left, and to
        # any point on the left-most column is the sum of all points above it.
        for i in range(1, row_count):
            cost[i][0] += cost[i - 1][0] + grid[i][0]
        for j in range(1, col_count):
            cost[0][j] += cost[0][j - 1] + grid[0][j]
        
        # The min cost to any point (i, j) is the cost of the point plus the
        # min cost to get to a point next to it, i.e. (i - 1, j) or (i, j - 1)
        for i in range(1, row_count):
            for j in range(1, col_count):
                cost[i][j] = min(cost[i - 1][j], cost[i][j - 1]) + grid[i][j]
        
        return cost[-1][-1]

s = Solution()
grid = [
         [1,3,1],
         [1,5,1],
         [4,2,1]
       ]
print(grid)
print(s.minPathSum(grid))

