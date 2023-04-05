from typing import List
from collections import Counter


class Solution:
    def squareFreeSubsets(self, nums: List[int]) -> int:
        def get_factor(x):
            factors = Counter()
            i = 2
            while x > 1:
                if x % i == 0:
                    factors[i] += 1
                    x //= i
                else:
                    i += 1
            return factors

        

        pass


def test_square_free_subsets():
    solution = Solution()
    assert solution.squareFreeSubsets([3, 4, 4, 5]) == 3, 'wrong result'
    assert solution.squareFreeSubsets([1]) == 1, 'wrong result'


if __name__ == '__main__':
    test_square_free_subsets()
