from typing import List
from functools import lru_cache
from math import gcd


class Solution:
    def simplifiedFractions1(self, n: int) -> List[str]:
        @lru_cache(None)
        def gcd(x, y):
            if y == 0:
                return x
            return gcd(y, x % y)

        res = list()
        for i in range(1, n):
            for j in range(i+1, n+1):
                if gcd(i, j) == 1:
                    res.append(str(i) + '/' + str(j))
        return res


def test_simplified_fractions():
    solution = Solution()

    # assert set(solution.simplifiedFractions(2)) == {"1/2"}, 'wrong result'
    assert set(solution.simplifiedFractions(3)) == {"1/2", "1/3", "2/3"}, 'wrong result'
    assert set(solution.simplifiedFractions(4)) == {"1/2", "1/3", "1/4", "2/3", "3/4"}, 'wrong result'


if __name__ == '__main__':
    test_simplified_fractions()

