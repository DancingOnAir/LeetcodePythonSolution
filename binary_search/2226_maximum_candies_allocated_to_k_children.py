from typing import List


class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        left, right = 1, max(candies)
        while left <= right:
            mid = left + (right - left) // 2
            if sum(x // mid for x in candies) >= k:
                left = mid + 1
            else:
                right = mid - 1
        return left - 1


def test_maximum_candies():
    solution = Solution()
    assert solution.maximumCandies([5, 8, 6], 3) == 5, 'wrong result'
    assert solution.maximumCandies([2, 5], 11) == 0, 'wrong result'


if __name__ == '__main__':
    test_maximum_candies()
