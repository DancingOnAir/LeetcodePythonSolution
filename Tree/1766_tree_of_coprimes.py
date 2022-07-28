from typing import List
from math import gcd


class Solution:

    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
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

