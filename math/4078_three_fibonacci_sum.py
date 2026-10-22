class Solution:
    def threeFibonacciSum(self, n: int) -> bool:
        a, b, c = 0, 1, 1
        while a + b + c <= n:
            if a + b + c == n:
                return True
            a, b, c = b, c, b + c
        return False


def test_three_fibonacci_sum():
    solution = Solution()
    assert solution.threeFibonacciSum(16), 'wrong result'
    assert not solution.threeFibonacciSum(8), 'wrong result'
    assert solution.threeFibonacciSum(2), 'wrong result'


if __name__ == '__main__':
    test_three_fibonacci_sum()
