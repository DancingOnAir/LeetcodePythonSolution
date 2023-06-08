from typing import List
from math import inf
from itertools import accumulate
from functools import lru_cache


class Solution:
    # improved dfs
    def mergeStones(self, stones: List[int], k: int) -> int:
        n = len(stones)
        if (n - k) % (k - 1):
            return -1

        ps = list(accumulate([0] + stones))

        @lru_cache(None)
        def dfs(i, j):
            if i == j:
                return 0

            res = min(dfs(i, m) + dfs(m + 1, j) for m in range(i, j, k - 1))
            if (j - i) % (k - 1) == 0:
                res += ps[j + 1] - ps[i]
            return res
        return dfs(0, n - 1)

    # dfs
    def mergeStones1(self, stones: List[int], k: int) -> int:
        n = len(stones)
        if (n - k) % (k - 1):
            return -1

        ps = list(accumulate([0] + stones))
        # 表示把stones[i]到stones[j]合并成p堆的最低成本
        @lru_cache(None)
        def dfs(i, j, p):
            if i == j:
                return 0
            if p == 1:
                return 0 if i == j else dfs(i, j, k) + ps[j + 1] - ps[i]
            return min(dfs(i, m, 1) + dfs(m + 1, j, p - 1) for m in range(i, j, k - 1))
        return dfs(0, n - 1, 1)

    # TLE
    def mergeStones1(self, stones: List[int], k: int) -> int:
        n = len(stones)
        if k > 1 and (n - k) % (k - 1):
            return -1

        def dfs(arr):
            if len(arr) < k:
                return 0
            res = inf
            for i in range(len(arr) - k + 1):
                cur = sum(arr[i: i + k])
                res = min(res, dfs(arr[0: i] + [cur] + arr[i + k:]) + cur)
            return res
        return dfs(stones)


def test_merge_stones():
    solution = Solution()
    assert solution.mergeStones([3, 2, 4, 1], 2) == 20, 'wrong result'
    assert solution.mergeStones([3, 2, 4, 1], 3) == -1, 'wrong result'
    assert solution.mergeStones([3, 5, 1, 2, 6], 3) == 25, 'wrong result'


if __name__ == '__main__':
    test_merge_stones()
