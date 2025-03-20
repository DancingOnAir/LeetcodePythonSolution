class Solution:
    def sum(self, num1: int, num2: int) -> int:
        if num1 == 0:
            return num2

        carry = (num1 & num2) << 1
        num1 ^= num2
        return self.sum(carry, num1)

    def sum1(self, num1: int, num2: int) -> int:
        return num1 + num2


def test_sum():
    solution = Solution()
    assert solution.sum(12, 5) == 17, 'wrong result'
    assert solution.sum(-10, 4) == -6, 'wrong result'


if __name__ == '__main__':
    test_sum()
