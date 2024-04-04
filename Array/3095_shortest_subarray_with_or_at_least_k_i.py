from typing import List


class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        n, res = len(nums), float('inf')
        for i in range(n):
            for j in range(i, n):
                tot = 0
                for idx in range(i, j + 1):
                    tot |= nums[idx]
                if tot >= k:
                    res = min(res, j - i + 1)
        return res if res < float('inf') else -1


def test_minimum_subarray_length():
    solution = Solution()
    assert solution.minimumSubarrayLength([1, 2, 3], 2) == 1, 'wrong result'
    assert solution.minimumSubarrayLength([2, 1, 8], 10) == 3, 'wrong result'
    assert solution.minimumSubarrayLength([1, 2], 0) == 1, 'wrong result'


if __name__ == '__main__':
    test_minimum_subarray_length()
