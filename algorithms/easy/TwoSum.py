class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Map elements to their index
        s = {}
        for i, elt in enumerate(nums):
            if elt not in s:
                s[elt] = i
            else:
                # If a duplicate exists, then check if both add to target
                if 2 * elt == target:
                    return [s[elt], i]
        
        for elt in nums:
            if ((target - elt) in s):
                if (s[elt] != s[target - elt]):
                    return [s[elt], s[target - elt]]
        return None
    
s = Solution()
arr = [3, 3]
print(s.twoSum(arr, 6))

