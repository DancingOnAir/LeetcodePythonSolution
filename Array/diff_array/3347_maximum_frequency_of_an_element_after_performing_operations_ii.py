from typing import List
from collections import defaultdict


class Solution:
    # 数组A的差分数组为D，其中D[i]=A[i]-A[i-1](i>0)且D[0]=A[0]
    # A[i]的差分数组是D[i]， 而D[i]的前缀和是A[i]
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        diff = defaultdict(int)
        cnt = defaultdict(int)

        for x in nums:
            cnt[x] += 1
            diff[x]
            diff[x - k] += 1
            diff[x + k + 1] -= 1

        res = 0
        sum_diff = 0
        for x, d in sorted(diff.items()):
            sum_diff += d
            res = max(res, min(sum_diff, cnt[x] + numOperations))
        return res


def test_max_frequency():
    solution = Solution()
    assert solution.maxFrequency([1, 4, 5], 1, 2) == 2, 'wrong result'
    assert solution.maxFrequency([5, 11, 20, 20], 5, 1) == 2, 'wrong result'


if __name__ == '__main__':
    test_max_frequency()
