from typing import List


class Solution:
    def maximumPoints(self, enemyEnergies: List[int], currentEnergy: int) -> int:
        mi = min(enemyEnergies)
        if currentEnergy < mi:
            return 0
        return (sum(enemyEnergies) - mi + currentEnergy) // mi


def test_maximum_points():
    solution = Solution()
    assert solution.maximumPoints([3,2,2], 2) == 3, 'wrong result'
    assert solution.maximumPoints([2], 10) == 5, 'wrong result'


if __name__ == '__main__':
    test_maximum_points()
