from itertools import groupby


class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        return '01' not in s

    def checkOnesSegment1(self, s: str) -> bool:
        return sum(1 for k, g in groupby(s) if k == '1') <= 1


def test_check_ones_segment():
    solution = Solution()

    assert not solution.checkOnesSegment('1001'), 'wrong result'
    assert solution.checkOnesSegment('110'), 'wrong result'


if __name__ == '__main__':
    test_check_ones_segment()
