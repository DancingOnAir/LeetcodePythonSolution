from typing import List
from bisect import bisect_right


class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        n = len(prizePositions)
        dp = [0] * (n + 1)
        res = 0
        for i, v in enumerate(prizePositions):
            j = bisect_right(prizePositions, v - k - 1)
            dp[i + 1] = max(dp[i], i - j + 1)
            res = max(res, i - j + 1 + dp[j])

        return res


def test_maximize_win():
    solution = Solution()
    assert solution.maximizeWin([1, 1, 2, 2, 3, 3, 5], 2) == 7, 'wrong result'
    assert solution.maximizeWin([1, 2, 3, 4], 0) == 2, 'wrong result'


if __name__ == '__main__':
    test_maximize_win()
