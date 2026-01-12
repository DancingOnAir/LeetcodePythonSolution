from typing import List
from collections import defaultdict


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pre_sum = [0]
        for x in nums:
            pre_sum.append(pre_sum[-1] + (x == k))

        pos = defaultdict(list)
        for i, x in enumerate(nums):
            pos[k - x].append(i + 1)

        res = 0
        for p in pos.values():
            mx = float('-inf')
            for i, idx in enumerate(p):
                mx = max(mx, pre_sum[idx - 1] - i + 1)
                res = max(res, pre_sum[n] - pre_sum[idx] + i + mx)
        return res


def test_max_frequency():
    solution = Solution()
    assert solution.maxFrequency([1, 2, 3, 4, 5, 6], 1) == 2, 'wrong result'
    assert solution.maxFrequency([10, 2, 3, 4, 5, 5, 4, 3, 2, 2], 10) == 4, 'wrong result'


if __name__ == '__main__':
    test_max_frequency()
