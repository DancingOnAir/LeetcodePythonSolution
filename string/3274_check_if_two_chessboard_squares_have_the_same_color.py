class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        def helper(c):
            x, y = ord(c[0]) - ord('a'), ord(c[1]) - ord('1')
            return (x + y) % 2
        return helper(coordinate1) == helper(coordinate2)

    def checkTwoChessboards1(self, coordinate1: str, coordinate2: str) -> bool:
        x1, y1 = ord(coordinate1[0]) - 97, int(coordinate1[1])
        x2, y2 = ord(coordinate2[0]) - 97, int(coordinate2[1])
        return ((x1 & 1) == (x2 & 1)) == ((y1 & 1) == (y2 & 1))


def test_check_two_chessboards():
    solution = Solution()
    assert solution.checkTwoChessboards("h7", "c8"), 'wrong result'
    assert solution.checkTwoChessboards("a1", "c3"), 'wrong result'
    assert not solution.checkTwoChessboards("a1", "h3"), 'wrong result'


if __name__ == '__main__':
    test_check_two_chessboards()
