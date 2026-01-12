from typing import List
from math import factorial


class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        if complexity[0] > min(complexity) or complexity.count(complexity[0]) > 1:
            return 0
        return factorial(len(complexity) - 1) % (10 ** 9 + 7)

    def countPermutations1(self, complexity: List[int]) -> int:
        first = complexity[0]
        complexity.sort()
        if first > complexity[0] or (len(complexity) > 1 and first == complexity[1]):
            return 0
        return factorial(len(complexity) - 1) % (10 ** 9 + 7)


def test_count_permutations():
    solution = Solution()
    assert solution.countPermutations([1, 2, 3]) == 2, 'wrong result'
    assert solution.countPermutations([3, 3, 3, 4, 4, 4]) == 0, 'wrong result'


if __name__ == '__main__':
    test_count_permutations()
