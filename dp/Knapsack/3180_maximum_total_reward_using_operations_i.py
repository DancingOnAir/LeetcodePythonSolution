from typing import List
from functools import lru_cache
from bisect import bisect_left


class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        @lru_cache(None)
        def dfs(i, x):
            if i >= len(rewardValues):
                return x

            return max(dfs(i + 1, x), dfs(i + 1, x + rewardValues[i]) if rewardValues[i] > x else 0)

        rewardValues = list(set(rewardValues))
        rewardValues.sort()
        return dfs(0, 0)


def test_max_total_reward():
    solution = Solution()
    assert solution.maxTotalReward([6,13,9,19]) == 34, 'wrong result'
    assert solution.maxTotalReward([2,15,14,18]) == 35, 'wrong result'
    assert solution.maxTotalReward([1, 1, 3, 3]) == 4, 'wrong result'
    assert solution.maxTotalReward([1, 6, 4, 3, 2]) == 11, 'wrong result'


if __name__ == '__main__':
    test_max_total_reward()
