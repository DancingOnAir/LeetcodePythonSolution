from typing import List
from collections import Counter
from itertools import combinations


class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        m, n = len(str(nums[0])), len(nums)
        # 最大值C(n, 2) * m
        res = m * n * (n - 1) // 2
        cnt = [[0] * 10 for _ in range(m)]

        for x in nums:
            for i, v in enumerate(str(x)):
                res -= cnt[i][int(v)]
                cnt[i][int(v)] += 1
        return res

    # TLE
    def sumDigitDifferences1(self, nums: List[int]) -> int:
        def diff(x, y):
            return sum(a != b for a, b in zip(str(x), str(y)))

        res = 0
        cnt = Counter(nums)
        for x, y in combinations(cnt.keys(), 2):
            res += diff(x, y) * cnt[x] * cnt[y]
        return res


def test_sum_digit_differences():
    solution = Solution()
    assert solution.sumDigitDifferences([13, 23, 12]) == 4, 'wrong result'
    assert solution.sumDigitDifferences([10, 10, 10, 10]) == 0, 'wrong result'


if __name__ == '__main__':
    test_sum_digit_differences()
