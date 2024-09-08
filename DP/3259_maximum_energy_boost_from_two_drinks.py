from typing import List
from functools import lru_cache


class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        a = b = 0
        for i in range(len(energyDrinkA)):
            a, b = max(a + energyDrinkA[i], b), max(b + energyDrinkB[i], a)
        return max(a, b)

    def maxEnergyBoost1(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        n = len(energyDrinkA)

        @lru_cache(None)
        def dfs(i, A):
            if i == n:
                return 0

            if A:
                return max(dfs(i + 1, A) + energyDrinkA[i], dfs(i + 1, not A))
            return max(dfs(i + 1, A) + energyDrinkB[i], dfs(i + 1, not A))

        return max(dfs(0, True), dfs(0, False))


def test_max_energy_boost():
    solution = Solution()
    assert solution.maxEnergyBoost([1, 3, 1], [3, 1, 1]) == 5, 'wrong result'
    assert solution.maxEnergyBoost([4, 1, 1], [1, 1, 3]) == 7, 'wrong result'


if __name__ == '__main__':
    test_max_energy_boost()
