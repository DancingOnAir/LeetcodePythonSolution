from typing import List
from collections import Counter


class Solution:
    # 不能使用单调栈，贪心算法，因为这种情况[1, 1, 2, 2, 3, 3]
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        max_val = max(cnt.values())
        if max_val <= len(nums) // 2:
            if len(nums) & 1:
                return 1
            return 0
        # 对多的值抵消掉其他的值 max_val - (n - max_val)
        return 2 * max_val - len(nums)

    def minLengthAfterRemovals1(self, nums: List[int]) -> int:
        n = len(nums)
        res = n
        i, j = 0, (n + 1) // 2
        while i < n // 2 and j < n:
            if nums[i] < nums[j]:
                res -= 2
            i += 1
            j += 1
        return res


def test_min_length_after_removals():
    solution = Solution()
    assert solution.minLengthAfterRemovals([1, 1, 1, 1, 1, 1, 1, 2, 2]) == 5, 'wrong result'
    assert solution.minLengthAfterRemovals([1, 1, 2, 2]) == 0, 'wrong result'
    assert solution.minLengthAfterRemovals([1, 2, 3, 4]) == 0, 'wrong result'
    assert solution.minLengthAfterRemovals([1, 1, 2, 2, 3, 3]) == 0, 'wrong result'
    assert solution.minLengthAfterRemovals([1000000000, 1000000000]) == 2, 'wrong result'
    assert solution.minLengthAfterRemovals([2, 3, 4, 4, 4]) == 1, 'wrong result'


if __name__ == '__main__':
    test_min_length_after_removals()
