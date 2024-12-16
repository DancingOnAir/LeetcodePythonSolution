class Solution:
    def distinctIntegers(self, n: int) -> int:
        return 1 if n == 1 else n - 1


def test_distinct_integers():
    solution = Solution()
    assert solution.distinctIntegers(5) == 4, 'wrong result'
    assert solution.distinctIntegers(3) == 2, 'wrong result'


if __name__ == '__main__':
    test_distinct_integers()
