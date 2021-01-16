from typing import List


class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        s = sum(machines)
        n = len(machines)
        q, r = divmod(s, n)
        if r:
            return -1

        dp = [machines[0] - q] + [0] * (n - 1)
        res = machines[0] - q
        for i in range(1, n):
            dp[i] = dp[i - 1] + (machines[i] - q)
            res = max(res, abs(dp[i]), machines[i] - q)
        return res


def test_find_min_moves():
    solution = Solution()
    # assert solution.findMinMoves([1, 0, 5]) == 3, 'wrong result'
    assert solution.findMinMoves([0, 3, 0]) == 2, 'wrong result'
    assert solution.findMinMoves([0, 2, 0]) == -1, 'wrong result'


if __name__ == '__main__':
    test_find_min_moves()
