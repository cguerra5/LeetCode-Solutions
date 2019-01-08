class Solution:
    def threeSum(self, nums):
        """Solves the three-sum problem for a list of integers
        Given an array nums of n integers, finds all the elements a, b, c in 
        nums such that a + b + c = 0.
        
        :param nums: A list of integers to solve the three sum problem for.
        :type nums: List[int]
        :return: A list of three-element lists containing all the unique 
                 triples [a, b, c] in nums that add to 0.
        :rtype: List[List[int]]
        """
        solution_sets = set()
        nums.sort()
        
        n = len(nums)
        for i in range(0, n - 3):
            a = nums[i]
            start = i + 1
            end = n - 1
            
            while start < end:
                b = nums[start]
                c = nums[end]
                sum_ = (a + b + c)
                if sum_ == 0:
                    solution_sets.add((a, b, c))
                    end -= 1
                    start += 1
                elif sum_ > 0:
                    end -= 1
                else:
                    start += 1
        # Convert set of 3-tuples to a list of 3-element lists
        return list(map(list, solution_sets))

s = Solution()
nums = [-1, 0, 1, 2, -1, -4]
print(s.threeSum(nums))

