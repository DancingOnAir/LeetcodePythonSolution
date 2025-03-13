from typing import List
from collections import defaultdict


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        cnt = defaultdict(list)
        for x in nums:
            cnt[max(str(x))].append(x)

        res = -1
        for vals in cnt.values():
            if len(vals) > 1:
                res = max(res, vals[0] + vals[1])
        return res


def test_max_sum():
    solution = Solution()
    assert solution.maxSum([112, 131, 411]) == -1, 'wrong result'
    assert solution.maxSum([2536, 1613, 3366, 162]) == 5902, 'wrong result'
    assert solution.maxSum([51, 71, 17, 24, 42]) == 88, 'wrong result'


if __name__ == '__main__':
    test_max_sum()
