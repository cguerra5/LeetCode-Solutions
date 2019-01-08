class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        total = sum(nums)
        if (S + total) & 1 == 1:
            return 0
        
s = Solution()
S = 3
nums = [1, 1, 1, 1, 1]
print(s.findTargetSumWays(nums, S))
