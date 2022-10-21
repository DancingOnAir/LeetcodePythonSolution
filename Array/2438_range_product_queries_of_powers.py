from typing import List
from itertools import accumulate


class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        powers = list()
        i = 0
        while n:
            if n & 1:
                powers.append(2 ** i)
            n >>= 1
            i += 1

        powers = list(accumulate(powers, lambda x, y: x * y))
        return [powers[e] % (10 ** 9 + 7) if s == 0 else (powers[e] // powers[s - 1]) % (10 ** 9 + 7) for s, e in queries]


def test_product_queries():
    solution = Solution()
    assert solution.productQueries(15, [[0, 1], [2, 2], [0, 3]]) == [2, 4, 64], 'wrong result'
    assert solution.productQueries(2, [[0, 0]]) == [2], 'wrong result'


if __name__ == '__main__':
    test_product_queries()
