from typing import List
from collections import defaultdict
from functools import cache


class Solution:
    # trie + floyd
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        len_to_str = defaultdict(set)
        dist = defaultdict(lambda: defaultdict(lambda: float('inf')))
        for x, y, c in zip(original, changed, cost):
            len_to_str[len(x)].add(x)
            len_to_str[len(y)].add(y)

            dist[x][y] = min(dist[x][y], c)
            dist[x][x] = 0
            dist[y][y] = 0

        for strs in len_to_str.values():
            for k in strs:
                for i in strs:
                    if dist[i][k] == float('inf'):
                        continue
                    for j in strs:
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        @cache
        def dfs(i):
            if i == 0:
                return 0
            res = float('inf')
            if source[i - 1] == target[i - 1]:
                res = dfs(i - 1)
            for sz, strs in len_to_str.items():
                if i < sz:
                    continue
                s = source[i - sz: i]
                t = target[i - sz: i]
                if s in strs and t in strs:
                    res = min(res, dist[s][t] + dfs(i - sz))
            return res
        ans = dfs(len(source))
        return ans if ans < float('inf') else -1


def test_minimum_cost():
    solution = Solution()
    assert solution.minimumCost("abcd", "acbe", ["a", "b", "c", "c", "e", "d"], ["b", "c", "b", "e", "b", "e"],
                                [2, 5, 5, 1, 2, 20]) == 28, 'wrong result'
    assert solution.minimumCost("abcdefgh", "acdeeghh", ["bcd", "fgh", "thh"], ["cde", "thh", "ghh"],
                                [1, 3, 5]) == 9, 'wrong result'
    assert solution.minimumCost("abcdefgh", "addddddd", ["bcd", "defgh"], ["ddd", "ddddd"],
                                [100, 1578]) == -1, 'wrong result'


if __name__ == '__main__':
    test_minimum_cost()
