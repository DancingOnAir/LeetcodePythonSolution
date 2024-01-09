from typing import List
from functools import cache


class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        dist = [[float('inf')] * 26 for _ in range(26)]
        for i in range(26):
            dist[i][i] = 0

        for x, y, c in zip(original, changed, cost):
            i = ord(x) - ord('a')
            j = ord(y) - ord('a')
            dist[i][j] = min(dist[i][j], c)

        # recursive method
        # @cache
        # def dfs(k, i, j):
        #     if k < 0:
        #         return dist[i][j]
        #     return min(dfs(k - 1, i, j), dfs(k - 1, i, k) + dfs(k - 1, k, j))
        #
        # res = 0
        # for x, y in zip(source, target):
        #     res += dfs(25, ord(x) - ord('a'), ord(y) - ord('a'))

        # loop method
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        res = sum(dist[ord(x) - ord('a')][ord(y) - ord('a')] for x, y in zip(source, target))
        return res if res < float('inf') else - 1


def test_minimum_cost():
    solution = Solution()
    assert solution.minimumCost("abcd", "acbe", ["a", "b", "c", "c", "e", "d"], ["b", "c", "b", "e", "b", "e"],
                                [2, 5, 5, 1, 2, 20]) == 28, 'wrong result'
    assert solution.minimumCost("aaaa", "bbbb", ["a", "c"], ["c", "b"], [1, 2]) == 12, 'wrong result'
    assert solution.minimumCost("abcd", "abce", ["a"], ["e"], [10000]) == -1, 'wrong result'


if __name__ == '__main__':
    test_minimum_cost()
