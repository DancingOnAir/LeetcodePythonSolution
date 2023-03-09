from typing import List


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left, right = 1, max(nums)
        while left <= right:
            mid = left + (right - left) // 2
            if sum((x - 1 + mid) // mid for x in nums) > threshold:
                left = mid + 1
            else:
                right = mid - 1
        return left


def test_smallest_divisor():
    solution = Solution()
    assert solution.smallestDivisor([1, 2, 5, 9], 6) == 5, 'wrong result'
    assert solution.smallestDivisor([44, 22, 33, 11, 1], 5) == 44, 'wrong result'


if __name__ == '__main__':
    test_smallest_divisor()
