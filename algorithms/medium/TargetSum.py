class Solution:
    def findTargetSumWays(self, nums, S):
        """
        Given a list of non-negative integers, a1, a2, ..., an, and a
        target S, each integer can be assigned + or -. 

        This returns the number of ways to assign symbols to make sum of 
        integers equal to target S.

        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        # Zero's can be appended to any solution set; ergo, the number of ways
        # n number of zeros adds to the final solution is constant. Hence, the
        # zeros are taken out and added later on to the final number of ways
        zero_count = nums.count(0)
        nums = [x for x in nums if x != 0]
        
        # This problem is equivalent to finding the set of positive integers
        # in nums that add to (S + sum(nums)) / 2. Since nums consists of
        # integers, no such set can exist if S + sum(nums) is odd.
        total = sum(nums)
        if S > total or (S + total) & 1 == 1:
            return 0
        target = (S + total) // 2
        
        # dp[i][j] holds the number of subsets consisting of elements from
        # nums[0] to nums[j - 1] that add to i.
        # dp[0][j] will then equal 1 for any j since any set can add to zero by
        # excluding all items.
        n = len(nums)
        dp = [[int(j == 0) for _ in range(n + 1)] for j in range(capacity + 1)]
        
        # This is a Subset-Sum problem where the target sum = (S + total) // 2
        # see https://en.wikipedia.org/wiki/Subset_sum_problem
        for cap in range(1, target + 1):
            for val in range(1, n + 1):
                dp[cap][val] = dp[cap][val - 1]
                if nums[val - 1] <= cap:
                    dp[cap][val] += dp[cap - nums[val - 1]][val - 1]
        
        # Any subset of the set of zeros Z in nums can be appended to any set
        # in the set of solutions. This then increases the number of solutions
        # by a factor of the number of elements in the power set of Z, i.e.
        # 2 ^ zero_count.
        return dp[capacity][n] * pow(2, zero_count)

s = Solution()
S = 0
nums = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
print(s.findTargetSumWays(nums, S))
