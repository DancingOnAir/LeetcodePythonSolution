from typing import List
from collections import Counter


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        res = cnt = 0
        seen = set()
        for x in nums[::-1]:
            res += 1
            if x not in seen:
                if x <= k:
                    cnt += 1
                seen.add(x)
            if cnt == k:
                return res


def test_min_operations():
    solution = Solution()
    assert solution.minOperations([3, 1, 5, 4, 2], 2) == 4, 'wrong result'
    assert solution.minOperations([3, 1, 5, 4, 2], 5) == 5, 'wrong result'
    assert solution.minOperations([3, 2, 5, 3, 1], 3) == 4, 'wrong result'


if __name__ == '__main__':
    test_min_operations()
