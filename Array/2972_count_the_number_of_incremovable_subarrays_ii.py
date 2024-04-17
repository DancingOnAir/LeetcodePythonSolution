from typing import List


class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i < n - 1 and nums[i] < nums[i + 1]:
            i += 1
        if i == n - 1:
            return n * (n + 1) // 2

        # 可以移除[i + 1, j - 1], [i, j - 1], [i - 1, j - 1], ..., [0, j - 1], 一共i + 2个, i = -1时，只能移除前缀[0, j - 1]
        res = i + 2
        j = n - 1
        while j == n - 1 or nums[j] < nums[j + 1]:
            while i >= 0 and nums[i] >= nums[j]:
                i -= 1
            res += i + 2
            j -= 1

        return res


def test_incremovable_subarray_count():
    solution = Solution()
    assert solution.incremovableSubarrayCount([1, 2, 3, 4]) == 10, 'wrong result'
    assert solution.incremovableSubarrayCount([6, 5, 7, 8]) == 7, 'wrong result'
    assert solution.incremovableSubarrayCount([8, 7, 6, 6]) == 3, 'wrong result'


if __name__ == '__main__':
    test_incremovable_subarray_count()
