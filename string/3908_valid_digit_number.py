class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        has_x = False
        while n >= 10:
            if n % 10 == x:
                has_x = True
            n //= 10
        return has_x and n != x


def test_valid_digit():
    solution = Solution()
    assert solution.validDigit(101, 0), 'wrong result'
    assert not solution.validDigit(232, 2), 'wrong result'
    assert not solution.validDigit(5, 1), 'wrong result'


if __name__ == '__main__':
    test_valid_digit()
