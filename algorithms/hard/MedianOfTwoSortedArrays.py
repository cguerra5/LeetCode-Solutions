import math

class Solution:
    def median(self, arr):
        """
        For a sorted array arr, find the median value.
        """
        middle = len(arr) // 2
        # Check if the size is even
        if len(arr) & 1 == 0:
            return (arr[middle - 1] + arr[middle]) / 2.0
        elif len(arr) > 0:
            return arr[middle]
        else:
            return None
    
    def medianWithNum(self, arr, num):
        """
        For a sorted array arr of numbers, finds the median value if the number
        num were to be inserted into the array.

        Arguements:
            arr (float[]):
                A sorted array of floats where len(arr) > 1.
        """
        combined_size = len(arr) + 1
        middle = len(arr) // 2
        # Check if the size is even
        if combined_size & 1 == 0:
            if combined_size == 2:
                return (arr[0] + num) / 2.0
            elif num < arr[middle + 1] and num > arr[middle - 1]:
                return (arr[middle] + num) / 2.0
            elif num < arr[middle - 1]:
                return (arr[middle] + arr[middle - 1]) / 2.0
            else:
                return (arr[middle] + arr[middle + 1]) / 2.0
        else:
            if num > arr[middle]:
                return arr[middle]
            elif num < arr[middle - 1]:
                return arr[middle - 1]
            else:
                return num
    
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        print(nums1)
        print(nums2)
        # Check if any of the lists are empty
        if not nums1 and nums2:
            return self.median(nums2)
        elif not nums2 and nums1:
            return self.median(nums1)
        elif not (nums1 or nums2):
            return None
        
        combined_size = len(nums1) + len(nums2)
        # Check base cases
        if len(nums1) == 1 and len(nums2) == 1:
            return (nums1[0] + nums2[0]) / 2.0
        if nums1[-1] <= nums2[0]:
            return self.median(nums1 + nums2)
        if nums2[-1] <= nums1[0]:
            return self.median(nums2 + nums1)
        #    return self.medianWithNum(nums2, nums1[0])
        #elif len(nums2) == 1:
        #    return self.medianWithNum(nums1, nums2[0])
        
        # Holds the location of each median in each list. This location will be
        # halfway between two indicies in the case of an even sized list
        med1_loc = len(nums1) / 2.0 
        med2_loc = len(nums2) / 2.0 
        
        med1 = self.median(nums1)
        med2 = self.median(nums2)
        
        print(med1)
        print(med2)
        print(med1_loc)
        print(med2_loc)
        print(' ')
        
        # med1 > med2 implies that the median m among the two arrays lies
        # in the elements in nums1 that are greater than med1 and the
        # elements in nums2 that are less than med2. Vice-versa for med1 < med2.
        n1 = nums1
        n2 = nums2
        if med1 > med2:
            n1 = n1[:math.ceil(med1_loc)]
            n2 = n2[math.ceil(med2_loc):]
        elif med1 < med2:
            n1 = n1[math.ceil(med1_loc):]
            n2 = n2[:math.ceil(med2_loc)]
        else:
            return med1  # Both arrays share the same median
        return self.findMedianSortedArrays(n1, n2)

s = Solution()
arr1 = [1, 2, 3, 5]
arr2 =         [4,  9, 10, 11, 12, 13, 14, 15, 16]
print('arr1 = {}\narr2 = {}'.format(arr1, arr2))
print(s.findMedianSortedArrays(arr1, arr2))

