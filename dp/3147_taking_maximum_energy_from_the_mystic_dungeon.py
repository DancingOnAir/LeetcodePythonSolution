from typing import List
from collections import defaultdict


class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n, res = len(energy), float('-inf')
        dp = [0] * n
        for i in range(n - 1, -1, -1):
            dp[i] = energy[i] + (dp[i + k] if i + k < n else 0)
            res = max(res, dp[i])
        return res


def test_maximum_energy():
    solution = Solution()
    assert solution.maximumEnergy([5, 2, -10, -5, 1], 3) == 3, 'wrong result'
    assert solution.maximumEnergy([-2, -3, -1], 2) == -1, 'wrong result'


if __name__ == '__main__':
    test_maximum_energy()
