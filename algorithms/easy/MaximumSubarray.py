class Solution:
    def maxSubArray(self, nums):
        """
        :param 
        :type nums: List[int]
        :return:
        :rtype: int
        """
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]
        
        max_sum = cur_sum = nums[0]
        
        for elt in nums[1:]:
            if cur_sum < 0:
                cur_sum = 0
            cur_sum += elt
            max_sum = max(max_sum, cur_sum)
        
        return max_sum

s = Solution()
nums = [-2,1]
print(s.maxSubArray(nums))

