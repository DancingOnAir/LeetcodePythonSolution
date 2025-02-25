from typing import List


class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        m = len(pizzas) // 4
        z, y = (m + 1) // 2, m // 2
        pizzas.sort(reverse=True)
        return sum(pizzas[:z] + pizzas[z+1: z+y+y+1: 2])


def test_max_weight():
    solution = Solution()
    assert solution.maxWeight([1, 2, 3, 4, 5, 6, 7, 8]) == 14, 'wrong result'
    assert solution.maxWeight([2, 1, 1, 1, 1, 1, 1, 1]) == 3, 'wrong result'


if __name__ == '__main__':
    test_max_weight()
