from typing import List
from collections import defaultdict


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        seen = set()
        cnt = 0
        for x in reversed(nums):
            if x not in seen:
                cnt += 1
                seen.add(x)
            else:
                break
        return (len(nums) - cnt + 2) // 3

    def minOperations1(self, nums: List[int]) -> int:
        res = 0
        m = defaultdict(int)
        for i, x in enumerate(nums):
            if x in m:
                res = max(res, (m[x] + 3) // 3)
            m[x] = i
        return res


def test_min_operations():
    solution = Solution()
    assert solution.minOperations([3, 8, 3, 6, 5, 8]) == 1, 'wrong result'
    assert solution.minOperations([2, 2]) == 1, 'wrong result'
    assert solution.minOperations([4, 3, 5, 1, 2]) == 0, 'wrong result'


if __name__ == '__main__':
    test_min_operations()
