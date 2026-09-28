class Solution:
    def minQueenMoves(self, source: list[int], target: list[int]) -> int:
        dx = abs(source[0] - target[0])
        dy = abs(source[1] - target[1])
        if dx == dy == 0:
            return 0
        if dx == dy or source[0] == target[0] or source[1] == target[1]:
            return 1
        return 2


def test_min_queen_moves():
    solution = Solution()
    assert solution.minQueenMoves([8, 1], target=[1, 8]) == 1, 'wrong result'
    assert solution.minQueenMoves([4, 2], target=[1, 3]) == 2, 'wrong result'
    assert solution.minQueenMoves([1, 1], target=[1, 1]) == 0, 'wrong result'


if __name__ == '__main__':
    test_min_queen_moves()
