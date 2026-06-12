from typing import List
from collections import defaultdict, deque
from math import inf


class Solution:
    # https://leetcode.com/problems/minimum-score-after-removals-on-a-tree/discuss/2198665/Python-3-Explanation-with-pictures
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        # degree of each node
        in_degree = [0] * n
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            in_degree[u] += 1
            in_degree[v] += 1

        seen = set()
        dq = deque()
        total_score = 0
        for i in range(n):
            total_score ^= nums[i]
            if in_degree[i] == 1:
                dq.append(i)
                seen.add(i)

        child = defaultdict(set)
        # subtree XOR value
        score = nums[:]
        while dq:
            u = dq.popleft()
            for v in graph[u]:
                # 'v is not in seen' means that node 'v' is the parent of node 'u'.
                if v not in seen:
                    child[v].add(u)
                    child[v] |= child[u]
                    score[v] ^= score[u]

                in_degree[v] -= 1
                if in_degree[v] == 1:
                    seen.add(v)
                    dq.append(v)

        res = inf
        for i in range(len(edges) - 1):
            for j in range(i+1, len(edges)):
                # let a & c be the lower break points
                a, b = edges[i]
                if b in child[a]:
                    a, b = b, a

                c, d = edges[j]
                if d in child[c]:
                    c, d = d, c

                if c in child[a]:
                    cur = [score[c], score[a] ^ score[c], total_score ^ score[a]]
                elif a in child[c]:
                    cur = [score[a], score[a] ^ score[c], total_score ^ score[c]]
                else:
                    cur = [score[a], score[c], total_score ^ score[a] ^ score[c]]
                res = min(res, max(cur) - min(cur))
        return res

    # https://leetcode.com/problems/minimum-score-after-removals-on-a-tree/discuss/2198386/Python3-dfs
    def minimumScore1(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def postorder(u, parent):
            score[u] = nums[u]
            child[u] = {u}
            for v in graph[u]:
                if v != parent:
                    score[u] ^= postorder(v, u)
                    child[u] |= child[v]

            return score[u]

        score = [0] * n
        child = [set() for _ in range(n)]
        postorder(0, -1)

        res = float('inf')
        for u in range(1, n):
            for v in range(u+1, n):
                if u in child[v]:
                    uu = score[u]
                    vv = score[v] ^ score[u]
                    xx = score[0] ^ score[v]
                elif v in child[u]:
                    uu = score[u] ^ score[v]
                    vv = score[v]
                    xx = score[0] ^ score[u]
                else:
                    uu = score[u]
                    vv = score[v]
                    xx = score[0] ^ score[u] ^ score[v]
                res = min(res, max(uu, vv, xx) - min(uu, vv, xx))
        return res


def test_minimum_score():
    solution = Solution()
    assert solution.minimumScore([1, 5, 5, 4, 11], [[0, 1], [1, 2], [1, 3], [3, 4]]) == 9, 'wrong result'
    assert solution.minimumScore([5, 5, 2, 4, 4, 2], [[0, 1], [1, 2], [5, 2], [4, 3], [1, 3]]) == 0, 'wrong result'


if __name__ == '__main__':
    test_minimum_score()

