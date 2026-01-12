from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        def dfs_helper(start, n):
            self.dist, self.parent = [-1] * n, [-1] * n
            self.dist[start] = 0
            dfs(start)
            return self.dist.index(max(self.dist))

        def dfs(start):
            for nei in g[start]:
                if self.dist[nei] == -1:
                    self.dist[nei] = self.dist[start] + 1
                    self.parent[nei] = start
                    dfs(nei)

        g = [set() for _ in range(n)]
        for u, v in edges:
            g[u].add(v)
            g[v].add(u)

        node1 = dfs_helper(0, n)
        node2 = dfs_helper(node1, n)

        path = list()
        while node2 != -1:
            path.append(node2)
            node2 = self.parent[node2]

        l = len(path)
        return list(set([path[l // 2], path[(l - 1) // 2]]))

    # TLE, dfs
    def findMinHeightTrees1(self, n: int, edges: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        def dfs(u, p):
            depth = 0
            for v in g[u]:
                if v != p:
                    depth = max(depth, 1 + dfs(v, u))
            return depth if depth else 1

        heights = list()
        min_height = n
        for i in range(n):
            heights.append(dfs(i, -1))
            min_height = min(min_height, heights[-1])
        return [i for i in range(n) if heights[i] == min_height]


def test_find_min_height_trees():
    solution = Solution()
    assert solution.findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]]) == [1], 'wrong result'
    assert solution.findMinHeightTrees(6, [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]) == [3, 4], 'wrong result'


if __name__ == '__main__':
    test_find_min_height_trees()

