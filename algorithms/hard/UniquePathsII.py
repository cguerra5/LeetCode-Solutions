class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        Returns the number of unique paths from the top left corner of an m x n
        grid to the bottom right corner, where 0 denotes empty space and 1 
        denotes an obstacle in the grid. Here, the agent moving from the top
        left to the bottom right can only move to the right and downward.
        
        :param obstacleGrid: A 2d array of integers representing the workspace
                             where 1 represents an obstacle and 0 represents 
                             empty space.
        :type obstacleGrid: List[List[int]]
        :return: The number of unique paths from the top left corner to the
                 bottom right corner where movement is limited to either going 
                 right or going downward.
        :rtype: int
        """
        if not obstacleGrid:
            return 0
        elif not obstacleGrid[0]:
            return 0
        
        # Create a 2d list of zeros with the same dimensions as obstacleGrid to
        # memoize results later on.
        row_count = len(obstacleGrid)
        col_count = len(obstacleGrid[0])
        path_count = [[0 for _ in range(col_count)] for _ in range(row_count)]
        
        # If there is an obstacle at the initial position, then no paths exist
        if obstacleGrid[0][0] == 1:
            return 0
        else:
            path_count[0][0] = 1
         
        # The robot can only move to the right and down. Hence, the number of 
        # paths from the top left point to any point j on the top row is either
        # 1 or 0 if there is an obstacle to the left of j. Likewise, any point
        # i on the first column is 1 or 0 if there is an obstacle above i
        for i in range(1, row_count):
            if obstacleGrid[i][0] == 1:
                break
            path_count[i][0] = 1
        for j in range(1, col_count):
            if obstacleGrid[0][j] == 1:
                break
            path_count[0][j] = 1
        
        # The number of paths at any given point (i, j) is equivalent to the
        # sum of the number of paths to the point above it and the point to the
        # left of it, (i, j - 1) and (i - 1, j) respectively.
        for i in range(1, row_count):
            for j in range(1, col_count):
                if obstacleGrid[i][j] != 1:
                    path_count[i][j] = path_count[i][j - 1] + path_count[i - 1][j]
        
        return path_count[-1][-1]
            
s = Solution()
grid = [
        []
       ]
print(s.uniquePathsWithObstacles(grid))
