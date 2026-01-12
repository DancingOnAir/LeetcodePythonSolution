class Solution:
    # bit manipulation
    def smallestEvenMultiple(self, n: int) -> int:
        return n << (n & 1)

    def smallestEvenMultiple1(self, n: int) -> int:
        return n * 2 if n & 1 else n


def test_smallest_even_multiple():
    solution = Solution()
    assert solution.smallestEvenMultiple(5) == 10, 'wrong result'
    assert solution.smallestEvenMultiple(6) == 6, 'wrong result'


if __name__ == '__main__':
    test_smallest_even_multiple()
