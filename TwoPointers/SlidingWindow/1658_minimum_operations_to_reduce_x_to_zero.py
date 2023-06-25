from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total = sum(nums)
        if total < x:
            return -1

        n = len(nums)
        if total == x:
            return n

        left = cur = 0
        res = n + 1
        for right, val in enumerate(nums):
            cur += val
            while left <= right and total - cur <= x:
                if total - cur == x:
                    res = min(res, n - (right - left + 1))
                cur -= nums[left]
                left += 1

        return res if res <= n else -1


def test_min_operations():
    solution = Solution()
    assert solution.minOperations([1, 1, 4, 2, 3], 5) == 2, 'wrong result'
    assert solution.minOperations([5, 6, 7, 8, 9], 4) == -1, 'wrong result'
    assert solution.minOperations([3, 2, 20, 1, 1, 3], 10) == 5, 'wrong result'


if __name__ == '__main__':
    test_min_operations()
