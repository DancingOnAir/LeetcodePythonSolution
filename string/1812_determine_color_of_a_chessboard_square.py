class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        return (ord(coordinates[0]) + int(coordinates[1])) & 1

    def squareIsWhite1(self, coordinates: str) -> bool:
        return (ord(coordinates[0]) & 1) ^ (int(coordinates[1]) & 1)


def test_square_is_white():
    solution = Solution()
    assert not solution.squareIsWhite('a1'), 'wrong result'
    assert solution.squareIsWhite('h3'), 'wrong result'
    assert not solution.squareIsWhite('c7'), 'wrong result'


if __name__ == '__main__':
    test_square_is_white()
