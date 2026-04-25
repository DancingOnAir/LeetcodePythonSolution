class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        return [sum(r) for r in matrix]

    def findDegrees1(self, matrix: list[list[int]]) -> list[int]:
        return list(map(sum, zip(*matrix)))


def test_find_degrees():
    solution = Solution()
    assert solution.findDegrees([[0, 1, 1], [1, 0, 1], [1, 1, 0]]) == [2, 2, 2], 'wrong result'
    assert solution.findDegrees([[0, 1, 0], [1, 0, 0], [0, 0, 0]]) == [1, 1, 0], 'wrong result'
    assert solution.findDegrees([[0]]) == [0], 'wrong result'


if __name__ == '__main__':
    test_find_degrees()
