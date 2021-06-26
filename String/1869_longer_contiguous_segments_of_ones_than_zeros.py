from itertools import groupby


class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        cnt = [[k, len(list(g))] for k, g in groupby(s)]

        zeros = ones = 0
        for i in cnt:
            if i[0] == '0' and i[1] > zeros:
                zeros = i[1]
            elif i[0] == '1' and i[1] > ones:
                ones = i[1]

        return zeros < ones


def test_check_zero_ones():
    solution = Solution()

    assert solution.checkZeroOnes('1101'), 'wrong result'
    assert not solution.checkZeroOnes('111000'), 'wrong result'
    assert not solution.checkZeroOnes('110100010'), 'wrong result'


if __name__ == '__main__':
    test_check_zero_ones()
