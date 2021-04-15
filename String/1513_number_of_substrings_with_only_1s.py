from itertools import groupby


class Solution:
    def numSub(self, s: str) -> int:
        res = 0

        for k, g in groupby(s):
            if k == '1':
                n = len(list(g))
                res += n * (n + 1) // 2
        return res % (10 ** 9 + 7)


def test_num_sub():
    solution = Solution()
    assert solution.numSub('0110111') == 9, 'wrong result'
    assert solution.numSub('101') == 2, 'wrong result'
    assert solution.numSub('111111') == 21, 'wrong result'
    assert solution.numSub('000') == 0, 'wrong result'


if __name__ == '__main__':
    test_num_sub()
