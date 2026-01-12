from typing import List
from bisect import bisect_right


class Solution:
    # https://leetcode.com/problems/maximize-win-from-two-segments/solutions/3141449/java-c-python-dp-sliding-segment-o-n/
    # sliding window + dp
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        n = len(prizePositions)
        dp = [0] * (n + 1)
        res = j = 0
        for i, v in enumerate(prizePositions):
            while prizePositions[j] < prizePositions[i] - k:
                j += 1
            dp[i + 1] = max(dp[i], i - j + 1)
            res = max(res, dp[j] + i - j + 1)
        return res

    # binary search + dp
    def maximizeWin1(self, prizePositions: List[int], k: int) -> int:
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
