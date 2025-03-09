from typing import List


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        flags = [True] * len(baskets)
        placed = 0
        for x in fruits:
            for i, y in enumerate(baskets):
                if y >= x and flags[i]:
                    placed += 1
                    flags[i] = False
                    break
        return len(fruits) - placed


def test_num_Of_unplaced_fruits():
    solution = Solution()
    assert solution.numOfUnplacedFruits([4, 2, 5], baskets=[3, 5, 4]) == 1, 'wrong result'
    assert solution.numOfUnplacedFruits([3, 6, 1], baskets=[6, 4, 7]) == 0, 'wrong result'


if __name__ == '__main__':
    test_num_Of_unplaced_fruits()
