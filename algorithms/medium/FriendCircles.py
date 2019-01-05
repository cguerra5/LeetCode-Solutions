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

class Solution:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if not M or not M[0]:
            return 0
        
        n = len(M)
        friend_circles = UnionFind(n)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if M[i][j] == 1:
                    friend_circles.union(i, j)
        
        return friend_circles.count()

s = Solution()
M = [[1,1,0],
     [1,1,1],
     [0,1,1]]

print(s.findCircleNum(M))


