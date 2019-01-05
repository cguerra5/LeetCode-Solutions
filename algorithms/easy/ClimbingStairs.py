class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        elif n == 1:
            return 1
        
        prev_steps = [1, 2]
        for i in range(2, n):
            next_step = prev_steps[0] + prev_steps[1]
            prev_steps[0], prev_steps[1] = prev_steps[1], next_step
        return prev_steps[1]

s = Solution()
print(s.climbStairs(5))
