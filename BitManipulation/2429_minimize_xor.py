class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        one1 = sum(map(int, bin(num1)[2:]))
        one2 = sum(map(int, bin(num2)[2:]))

        if one1 > one2:
            diff = one1 - one2
            while diff:
                num1 = num1 & (num1 - 1)
                diff -= 1
            return num1
        elif one1 < one2:
            diff = one2 - one1
            res = ''

            for c in bin(num1)[2:][::-1]:
                if c == '0' and diff > 0:
                    res += '1'
                    diff -= 1
                else:
                    res += c

            while diff:
                res += '1'
                diff -= 1

            return int(res[::-1], 2)
        return num1


def test_minimize_xor():
    solution = Solution()
    assert solution.minimizeXor(65, 84) == 67, 'wrong result'
    assert solution.minimizeXor(25, 72) == 24, 'wrong result'
    assert solution.minimizeXor(3, 5) == 3, 'wrong result'
    assert solution.minimizeXor(1, 12) == 3, 'wrong result'


if __name__ == '__main__':
    test_minimize_xor()
