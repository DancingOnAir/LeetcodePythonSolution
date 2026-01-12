class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        return num.rstrip('0')

    def removeTrailingZeros2(self, num: str) -> str:
        res = int(num)
        while res and res % 10 == 0:
            res //= 10
        return str(res)

    def removeTrailingZeros1(self, num: str) -> str:
        if len(num) == 1:
            return num

        num = list(num)
        while num[-1] == '0':
            num.pop()
        return ''.join(num)


def test_remove_trailing_zeros():
    solution = Solution()
    assert solution.removeTrailingZeros("51230100") == "512301", 'wrong result'
    assert solution.removeTrailingZeros("123") == "123", 'wrong result'


if __name__ == '__main__':
    test_remove_trailing_zeros()
