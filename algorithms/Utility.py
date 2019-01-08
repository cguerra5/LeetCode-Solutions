class UnionFind:
    def __init__(self, n):
        """
        Initializes a disjoint-set data structure of n elements where each
        element is considered to be in its own set.
        
        :param n: The total number of elements among all the sets.
        :type n: int
        """
        # For an index i, parents[i] is the parent of i.
        self.parents = [i for i in range(n)]
        # For an index i, holds the size for the tree containing i.
        self.size = [1 for _ in range(n)]
        # Keeps count of the number of trees, i.e. the number of disjoint sets
        self.set_count = n
    
    def root(self, p):
        """Finds the root of an element at index p.
        
        :param p: The index of an element in parents[].
        :type p: int
        :return: The index of the root of parents[p].
        :rtype: int
        """
        while p != self.parents[p]:
            self.parents[p] = self.parents[self.parents[p]]  # Path compression
            p = self.parents[p]
        return p
    
    def union(self, elt1, elt2):
        """Merges the sets which two elements belong to.
        
        :param elt1: The index of the first element.
        :type elt1: int
        :param elt2: The index of the second element.
        :type elt1: int
        """
        root1 = self.root(elt1)
        root2 = self.root(elt2)
        
        # If the roots match, then the elements already belong to the same set
        if root1 == root2:
            return
        
        # Merge the smaller set into the larger set
        if self.size[root2] > self.size[root1]:
            root1, root2 = root2, root1
        self.parents[root2] = root1
        self.size[root1] += self.size[root2]
        self.set_count -= 1
    
    def count(self):
        """Returns the number of disjoint sets. 
        
        :return: The number of distinct roots in parents[].
        :rtype: int
        """
        return self.set_count

def smallestLargerValue(arr, target):
    """
    For a sorted array arr, returns the index of the smallest value that
    is greater than target using a binary search. If dupicates of this
    value exist, then it finds the leftmost occurence.
    """
    left_bound = 0
    right_bound = len(arr)
    pivot = len(arr) // 2
    
    while (left_bound < right_bound):
        if (arr[pivot] > target):
            right_bound = pivot - 1
        elif (arr[pivot] <= target):
            # If the target equals the pivot, keep searching the right side
            # in case of dupicates
            left_bound = pivot + 1
        pivot = (left_bound + right_bound) // 2
    
    if arr[pivot] > target:
        return pivot
    else:
        return pivot + 1

def binarySearch(arr, target):
    """
    For a sorted array arr, returns the index of the smallest value that
    is greater than target using a binary search.
    """
    left_bound = 0
    right_bound = len(arr)
    pivot = len(arr) // 2
    
    while (left_bound < right_bound):
        if (arr[pivot] > target):
            right_bound = pivot - 1
        elif (arr[pivot] < target):
            left_bound = pivot + 1
        else:
            return pivot
        pivot = (left_bound + right_bound) // 2
    
    return None

