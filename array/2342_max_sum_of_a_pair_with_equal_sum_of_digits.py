from typing import List
from collections import defaultdict


class Solution:
    # two sum
    def maximumSum(self, nums: List[int]) -> int:
        res = -1
        m = dict()

        for num in nums:
            s = sum(int(d) for d in str(num))
            if s not in m:
                m[s] = num
            else:
                res = max(res, num + m[s])
                m[s] = max(m[s], num)
        return res

    def maximumSum1(self, nums: List[int]) -> int:
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

