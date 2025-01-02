from typing import List
from collections import Counter


class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        sorted_keys = sorted(cnt.keys(), key=lambda k: -cnt[k])
        if cnt[sorted_keys[0]] <= len(nums) - cnt[sorted_keys[0]] + 1:
            return -1

        cur = 0
        for i, x in enumerate(nums):
            if x == sorted_keys[0]:
                cur += 1
                if cur > i + 1 - cur:
                    return i
        return -1


def test_minimum_index():
    solution = Solution()
    assert solution.minimumIndex([1, 2, 2, 2]) == 2, 'wrong result'
    assert solution.minimumIndex([2, 1, 3, 1, 1, 1, 7, 1, 2, 1]) == 4, 'wrong result'
    assert solution.minimumIndex([3, 3, 3, 3, 7, 2, 2]) == -1, 'wrong result'


if __name__ == '__main__':
    test_minimum_index()

