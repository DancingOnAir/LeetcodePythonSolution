from typing import List
from collections import Counter
from functools import lru_cache


class Solution:
    # loop
    def maximumTotalDamage(self, power: List[int]) -> int:
        freq = Counter(power)
        sorted_keys = sorted(freq)
        dp = [0] * (len(sorted_keys) + 1)
        j = 0
        for i, x in enumerate(sorted_keys):
            while sorted_keys[j] < x - 2:
                j += 1
            dp[i + 1] = max(dp[i], dp[j] + x * freq[x])
        return dp[-1]

    # recursive
    def maximumTotalDamage1(self, power: List[int]) -> int:
        @lru_cache(None)
        def dfs(i):
            if i < 0:
                return 0
            x = sorted_keys[i]
            j = i
            while j and sorted_keys[j - 1] >= x - 2:
                j -= 1
            return max(dfs(i - 1), dfs(j - 1) + x * freq[x])

        freq = Counter(power)
        sorted_keys = sorted(freq.keys())
        return dfs(len(sorted_keys) - 1)


def test_maximum_total_damage():
    solution = Solution()
    assert solution.maximumTotalDamage([1,1,3,4]) == 6, 'wrong result'
    assert solution.maximumTotalDamage([7, 1, 6, 3]) == 10, 'wrong result'
    assert solution.maximumTotalDamage([1, 1, 3, 4]) == 6, 'wrong result'
    assert solution.maximumTotalDamage([7, 1, 6, 6]) == 13, 'wrong result'


if __name__ == '__main__':
    test_maximum_total_damage()
