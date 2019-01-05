class Solution:
    def rob(self, nums):
        """
        Finds the largest sum of non-adjacent elements in an array of
        non-negative integers.
        
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        elif n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1])
        
        memo = [nums[0], max(nums[1], nums[0]), max(nums[0] + nums[2], nums[1])]
        
        for elt in nums[3:]:
            max_sum = max(memo[0], memo[1]) + elt
            memo[0], memo[1], memo[2] = memo[1], memo[2], max_sum
        
        return max(memo[0], memo[1], memo[2])

s = Solution()
nums = [2, 7, 9, 3, 1]
print(s.rob(nums))
