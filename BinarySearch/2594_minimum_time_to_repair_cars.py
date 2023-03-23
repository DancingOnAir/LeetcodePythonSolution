from typing import List


class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        left, right = 0, max(ranks) * cars * cars // len(ranks) + 1
        while left <= right:
            mid = left + (right - left) // 2
            total = sum(int((mid / x) ** 0.5) for x in ranks)
            if total >= cars:
                right = mid - 1
            else:
                left = mid + 1
        return left


def test_repair_cars():
    solution = Solution()
    assert solution.repairCars([1, 1, 3, 3], 74) == 576, 'wrong result'
    assert solution.repairCars([4, 2, 3, 1], 10) == 16, 'wrong result'
    assert solution.repairCars([5, 1, 8], 6) == 16, 'wrong result'


if __name__ == '__main__':
    test_repair_cars()
