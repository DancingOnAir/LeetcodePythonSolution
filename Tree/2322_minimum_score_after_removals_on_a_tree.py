from typing import List
from collections import defaultdict


class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
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

