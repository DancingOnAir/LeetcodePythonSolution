class Solution:
    def smallestNumber(self, n: int) -> int:
        return (1 << (len(bin(n)) - 2)) - 1


def test_smallest_number():
    solution = Solution()
    assert solution.smallestNumber(5) == 7, 'wrong result'
    assert solution.smallestNumber(10) == 15, 'wrong result'
    assert solution.smallestNumber(3) == 3, 'wrong result'


if __name__ == '__main__':
    test_smallest_number()
