from typing import List
from collections import defaultdict


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def get_digit_sum(num):
            return sum(map(int, str(num)))

        m = defaultdict(list)
        for num in nums:
            m[get_digit_sum(num)].append(num)

        return max([sum(sorted(vals)[-2:]) for vals in m.values() if len(vals) > 1] + [-1])


def test_maximum_sum():
    solution = Solution()
    assert solution.maximumSum([18, 43, 36, 13, 7]) == 54, 'wrong result'
    assert solution.maximumSum([10, 12, 19, 14]) == -1, 'wrong result'


if __name__ == '__main__':
    test_maximum_sum()

