from functools import reduce


class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for i in range(n, n + 10):
            prod, val = 1, i
            while val:
                prod *= val % 10
                val //= 10
            if prod % t == 0:
                return i

    # simulation
    def smallestNumber1(self, n: int, t: int) -> int:
        while reduce(lambda x, y: x * y, map(int, str(n))) % t != 0:
            n += 1
        return n


def test_smallest_number():
    solution = Solution()
    assert solution.smallestNumber(10, 2) == 10, 'wrong result'
    assert solution.smallestNumber(15, 3) == 16, 'wrong result'


if __name__ == '__main__':
    test_smallest_number()
