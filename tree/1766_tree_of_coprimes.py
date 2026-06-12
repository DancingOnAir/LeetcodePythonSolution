from typing import List
from math import gcd
from collections import deque


class Solution:
    # bfs
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        def compute_gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        # m keeps the set of j which is coprime with i in [0, 50]
        m = {i: {j for j in range(51) if compute_gcd(i, j) == 1} for i in range(51)}
        n = len(nums)
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        res = [-1] * n
        seen = set()
        # the element is key: nums[node], val: list of parents' (node, depth)
        dq = deque([(0, {})])
        depth = 0

        while dq:
            sz = len(dq)
            for _ in range(sz):
                node, parents = dq.popleft()
                seen.add(node)
                overlap = m[nums[node]] & parents.keys()
                if overlap:
                    res[node] = parents[max(overlap, key=lambda x: parents[x][1])][0]
                for child in graph[node]:
                    if child not in seen:
                        p = parents.copy()
                        p[nums[node]] = (node, depth)
                        dq.append((child, p))
            depth += 1
        return res

    # dfs
    def getCoprimes3(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        n = len(nums)
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        # path: key-> nums[node], val->list of (node, depth)
        path = dict()
        seen = {0}

        def dfs(node, depth):
            last_depth = -1
            for x in path:
                if gcd(nums[node], x) == 1:
                    if path[x] and path[x][-1][1] > last_depth:
                        res[node] = path[x][-1][0]
                        last_depth = path[x][-1][1]

            path.setdefault(nums[node], []).append((node, depth))
            for child in graph[node]:
                if child not in seen:
                    seen.add(child)
                    dfs(child, depth + 1)
            path[nums[node]].pop()

        res = [-1] * n
        dfs(0, 0)
        return res

    # dfs
    def getCoprimes2(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        n = len(nums)
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        res = [-1] * n
        path = [[] for _ in range(51)]
        seen = set()

        def dfs(node, depth):
            if node in seen:
                return
            seen.add(node)
            max_depth = -1
            for x in range(1, 51):
                if gcd(nums[node], x) == 1:
                    if len(path[x]) > 0:
                        top_node, top_depth = path[x][-1]
                        if max_depth < top_depth:
                            max_depth = top_depth
                            res[node] = top_node
            path[nums[node]].append((node, depth))
            for child in graph[node]:
                dfs(child, depth + 1)
            path[nums[node]].pop()

        dfs(0, 0)
        return res

    # TLE
    def getCoprimes1(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        n = len(nums)
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def gcd(a, b):
            if a < b:
                a, b = b, a
            if a % b == 0:
                return b
            return gcd(b, a % b)

        def inorder(node, parent, path):
            if parent != -1:
                for p in path[::-1]:
                    if gcd(nums[node], nums[p]) == 1:
                        res[node] = p
                        break
                else:
                    res[node] = -1

            path.append(node)
            for child in graph[node]:
                if child != parent:
                    inorder(child, node, path)
            path.pop()

        res = [-1] * n
        inorder(0, -1, [])
        return res


def test_get_coprimes():
    solution = Solution()
    assert solution.getCoprimes([2, 3, 3, 2], [[0, 1], [1, 2], [1, 3]]) == [-1, 0, 0, 1], 'wrong result'
    assert solution.getCoprimes([5, 6, 10, 2, 3, 6, 15], [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]]) == [-1, 0, -1, 0, 0, 0, -1], 'wrong result'


if __name__ == '__main__':
    test_get_coprimes()

