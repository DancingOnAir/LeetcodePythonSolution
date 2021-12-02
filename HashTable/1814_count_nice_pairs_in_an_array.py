from typing import List
from collections import Counter

class Solution:
    def countNicePairs1(self, nums: List[int]) -> int:
        def calculate_diff(num):
            return int(''.join(reversed(str(num)))) - num

        diffs = dict()
        for num in nums:
            diffs.setdefault(calculate_diff(num), list()).append(num)

        res = 0
        mod = 10 ** 9 + 7
        for v in diffs.values():
            cur = len(v)
            res += cur * (cur - 1) // 2
        return res % mod

    def countNicePairs(self, nums: List[int]) -> int:
        diffs = Counter()
        res = 0
        for a in nums:
            b = int(str(a)[::-1])
            res += diffs[b - a]
            diffs[b - a] += 1
        return res % (10 ** 9 + 7)


def test_count_nice_pairs():
    solution = Solution()

    assert solution.countNicePairs([42, 11, 1, 97]) == 2, 'wrong result'
    assert solution.countNicePairs([13, 10, 35, 24, 76]) == 4, 'wrong result'


if __name__ == '__main__':
    test_count_nice_pairs()

