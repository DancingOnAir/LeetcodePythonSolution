from bisect import bisect_left
from collections import OrderedDict


class Solution:
    def __init__(self):
        self.memo = {0: 0}

    # bottom-up dp
    # https://leetcode.com/problems/race-car/discuss/227415/Figures-to-make-the-DP-solution-more-straightforward
    def racecar(self, target: int) -> int:
        dp = [0] + [0x3f3f3f3f] * target
        for i in range(1, target+1):
            m, j = 1, 1
            while j < i:
                p, q = 0, 0
                while p < j:
                    dp[i] = min(dp[i], m + 1 + q + 1 + dp[i - j + p])
                    q += 1
                    p = (1 << q) - 1
                m += 1
                j = (1 << m) - 1

            dp[i] = min(dp[i], m + (0 if i == j else 1 + dp[j - i]))
        return dp[target]

    # bfs
    def racecar2(self, target: int) -> int:
        if target in self.memo:
            return self.memo[target]

        n = target.bit_length()
        if 2 ** n - 1 == target:
            self.memo[target] = n
        else:
            self.memo[target] = self.racecar(2**n - 1 - target) + n + 1
            for m in range(n - 1):
                self.memo[target] = min(self.memo[target], self.racecar(target - 2**(n - 1) + 2**m) + n + m + 1)
        return self.memo[target]

    # bfs solution but failed
    # failure testing case, if the input 5, we can reach with only 7 steps: AARARAA
    def racecar1(self, target: int) -> int:
        if not target:
            return 0

        memo = dict()
        def min_steps(target):
            if target in memo:
                return memo[target]
            arr = sorted(memo.keys())
            pos = bisect_left(arr, target)

            positive_diff = target - arr[pos - 1]
            negative_diff = arr[pos] - target

            step = min(memo[arr[pos - 1]] + min_steps(positive_diff) + 2, memo[arr[pos]] + min_steps(negative_diff) + 1)
            memo[target] = step
            return step

        total, i, step = 0, 1, 0
        while total < target:
            total += i
            i *= 2
            step += 1
            memo[total] = step

        if target == total:
            return step
        return min(step + min_steps(total - target) + 1, step - 1 + min_steps(target - (total - i // 2)) + 2)


def test_race_car():
    solution = Solution()
    assert solution.racecar(3) == 2, 'wrong result'
    assert solution.racecar(6) == 5, 'wrong result'


if __name__ == '__main__':
    test_race_car()
