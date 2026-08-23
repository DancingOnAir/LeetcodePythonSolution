class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digit_sum = 0
        digit_prod = 1
        x = n
        while x > 0:
            r = x % 10
            digit_sum += r
            digit_prod *= r
            x //= 10
        return n % (digit_sum + digit_prod) == 0

def test_check_divisibility():
    solution = Solution()
    assert solution.checkDivisibility(99), 'wrong result'
    assert not solution.checkDivisibility(23), 'wrong result'


if __name__ == '__main__':
    test_check_divisibility()
