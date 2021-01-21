from bisect import bisect_left
from collections import OrderedDict


class Solution:
    def racecar(self, target: int) -> int:
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
    # assert solution.racecar(3) == 2, 'wrong result'
    assert solution.racecar(6) == 5, 'wrong result'


if __name__ == '__main__':
    test_race_car()
