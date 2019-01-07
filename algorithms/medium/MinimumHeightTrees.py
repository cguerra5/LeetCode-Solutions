import random as rand

class Solution:
    def furthestVertex(self, neighbors, root):
        """Find the furthest vertex from the root in an undirected tree.
        """
        # dist_to_root[i] holds the distance from the i-th vertex to the root
        dist_to_root = [0 for _ in range(len(neighbors))]
        
        # Do a DFS to determine the vertex that is furthest from the root
        furthest = 0
        verticies_seen = {root}
        stack = [root]
        while stack:
            parent = stack.pop()
            if dist_to_root[parent] > dist_to_root[furthest]:
                furthest = parent
            for v in neighbors[parent]:
                if v not in verticies_seen:
                    stack.append(v)
                    verticies_seen.add(v)
                    dist_to_root[v] = dist_to_root[parent] + 1
        return furthest
    
    def findPath(self, neighbors, v1, v2):
        """Finds a path from v1 to v2 in an undirected tree.
        """
        # Do a DFS to find a path from v1 to v2
        parents = {v1 : -1}
        stack = [v1]
        while stack:
            parent = stack.pop()
            if parent == v2:
                break
            for v in neighbors[parent]:
                if v not in parents:
                    stack.append(v)
                    parents[v] = parent
        
        # Construct the path from the history
        path = [v2]
        next_v = parents[v2]
        while next_v != -1:
            path.append(next_v)
            next_v = parents[next_v]
        
        return path
        
    
    def findMinHeightTrees(self, n, edges):
        """Gets roots of all the Minimum Height trees in an undirected tree.
        
        :param n: The number of verticies in the tree.
        :type n: int
        :param edges: A list of edges where an element [vi, vj] indicates that
                      an edge exists between vertex vi and vertex vj.
        :type edges: List[List[int]]
        :return: The indicies of the roots that form the Minimum Height Trees
                 in the tree.
        :rtype: List[int]
        """
        if n == 1:
            return [0]
        
        # neighbors[i] contains the indices of the neighbors of the i-th vertex
        neighbors = [[] for _ in range(n)]
        for (v1, v2) in edges:
            neighbors[v1].append(v2)
            neighbors[v2].append(v1)
        
        rand.seed(None)
        root = rand.randrange(n)
        
        # Find the two verticies that are the farthest away from one another.
        # These will be the end points of the longest path in the tree
        furthest1 = self.furthestVertex(neighbors, root)
        furthest2 = self.furthestVertex(neighbors, furthest1)
        
        # The roots with the minimum heights will be in the middle of the
        # longest path in the tree
        path = self.findPath(neighbors, furthest1, furthest2)
        path_len = len(path)
        # Test if the length is even
        if path_len & 1 == 0:
            return [path[(path_len // 2) - 1], path[path_len // 2]]
        else:
            return [path[path_len // 2]]

if __name__ == '__main__':
    s = Solution()
    n = 4
    edges = [[1, 0], [1, 2], [1, 3]]
    print(s.findMinHeightTrees(n, edges))

