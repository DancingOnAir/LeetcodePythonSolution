class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        res = list()
        while a or b:
            if len(res) >= 2 and res[-1] == res[-2]:
                write_a = (res[-1] == 'b')
            else:
                write_a = (a >= b)

            if write_a:
                res.append('a')
                a -= 1
            else:
                res.append('b')
                b -= 1

        return ''.join(res)

    def strWithout3a3b1(self, a: int, b: int) -> str:
        if not a:
            return 'b' * b
        if not b:
            return 'a' * a

        if b - a > 1:
            return 'bba' + self.strWithout3a3b(a - 1, b - 2)
        elif a - b > 1:
            return 'aab' + self.strWithout3a3b(a - 2, b - 1)
        elif b - a == 1:
            return 'ab' * a + 'b'
        elif a - b == 1:
            return 'ab' * b + 'a'

        return 'ab' * a


def test_str_without_3a3b():
    solution = Solution()
    assert solution.strWithout3a3b(1, 2) == "abb", 'wrong result'
    assert solution.strWithout3a3b(4, 1) == "aabaa", 'wrong result'


if __name__ == '__main__':
    test_str_without_3a3b()
