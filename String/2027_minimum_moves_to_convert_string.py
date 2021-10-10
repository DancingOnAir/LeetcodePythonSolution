class Solution:
    def minimumMoves(self, s: str) -> int:
        res = 0
        idx = s.find('X')
        while idx != -1:
            idx = s.find('X', idx+3)
            res += 1
        return res


def test_minimum_moves():
    solution = Solution()

    assert solution.minimumMoves("XXX") == 1, 'wrong result'
    assert solution.minimumMoves("XXOX") == 2, 'wrong result'
    assert solution.minimumMoves("OOOO") == 0, 'wrong result'


if __name__ == '__main__':
    test_minimum_moves()
