class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = tot = i = 0
        while n > 0:
            r = n % 10
            n //= 10
            if r == 0:
                continue
            x += r * (10 ** i)
            tot += r
            i += 1
        return x * tot


def test_sum_and_multiply():
    solution = Solution()
    assert solution.sumAndMultiply(10203004) == 12340, 'wrong result'
    assert solution.sumAndMultiply(1000) == 1, 'wrong result'


if __name__ == '__main__':
    test_sum_and_multiply()
