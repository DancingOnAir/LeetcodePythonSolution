from typing import List


class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        left, n, tot = 0, len(nums), 0
        q, r = divmod(target, sum(nums))
        res, target = n, r
        for right in range(2 * n):
            tot += nums[right % n]

            while tot >= target:
                if tot == target:
                    res = min(res, right - left + 1)
                tot -= nums[left % n]
                left += 1

        return res + q * n if res < n else -1


def test_min_size_subarray():
    solution = Solution()
    assert solution.minSizeSubarray([2,1,5,7,7,1,6,3], 39) == 9, 'wrong result'
    assert solution.minSizeSubarray([1, 2, 3], 5) == 2, 'wrong result'
    assert solution.minSizeSubarray([1, 1, 1, 2, 3], 4) == 2, 'wrong result'
    assert solution.minSizeSubarray([2, 4, 6, 8], 3) == -1, 'wrong result'


if __name__ == '__main__':
    test_min_size_subarray()
