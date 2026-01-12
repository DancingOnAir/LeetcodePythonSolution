class Solution:
    def minOperations(self, n: int) -> int:
        return (n * n - n % 2) // 4


def test_min_operations():
    solution = Solution()
    assert solution.minOperations(3) == 2, 'wrong result'
    assert solution.minOperations(6) == 9, 'wrong result'


if __name__ == '__main__':
    test_min_operations()
