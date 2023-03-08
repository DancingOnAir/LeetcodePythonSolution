from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        while left <= right:
            mid = left + (right - left) // 2
            if sum((x - 1) // mid + 1 for x in piles) > h:
                left = mid + 1
            else:
                right = mid - 1
        return left


def test_min_eating_speed():
    solution = Solution()
    assert solution.minEatingSpeed([3, 6, 7, 11], 8) == 4, 'wrong result'
    assert solution.minEatingSpeed([30, 11, 23, 4, 20], 5) == 30, 'wrong result'
    assert solution.minEatingSpeed([30, 11, 23, 4, 20], 6) == 23, 'wrong result'


if __name__ == '__main__':
    test_min_eating_speed()
