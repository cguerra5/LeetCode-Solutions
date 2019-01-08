class Solution:
    def canPartition(self, nums):
        """
        Finds if the array can be partitioned into two subsets such that the 
        sum of elements in both subsets is equal.
        
        :param nums: A non-empty list of positive integers.
        :type nums: List[int]
        :return: True if nums can be partitioned into two sets of equal sum.
        :rtype: bool
        """
        n = len(nums)
        total = sum(nums)
        
        # This problem is the equivalent to finding a set A that adds up to
        # half of the sum total of nums. Since the array is made up of integers,
        # this is impossible if the sum total is odd.
        if (total & 1) == 1:
            return False
        capacity = total // 2
        
        # dp[i][j], indicates whether or not a capacity j can be fulfilled
        # from a subset of the elements nums[0] to nums[i - 1], inclusive.
        # dp[i][0], will always be true since a capacity of zero can be
        # fulfilled by not including any elements
        dp = [[j == 0 for _ in range(n + 1)] for j in range(capacity + 1)]
        
        # An element is either a part of set A or it isn't; hence, this problem
        # reduces to the subset-sum problem.
        for cap in range(1, capacity + 1):
            for val in range(1, n + 1):
                dp[cap][val] = dp[cap][val- 1]
                if nums[val - 1] <= cap and not dp[cap][val]:
                    dp[cap][val] = dp[cap - nums[val - 1]][val - 1]
        
        return dp[capacity][n]

s = Solution()
nums = [1, 2, 3, 5]  # [1, 5, 11, 5] 
print(s.canPartition(nums))

