class Solution:
    def minBishopMoves(self, source: list[int], target: list[int]) -> int:
        if (source[0] % 2 != source[1] % 2) == (target[0] % 2 == target[1] % 2):
            return -1
        if abs(source[0] - target[0]) == abs(source[1] - target[1]):
            return 1
        return 2


def test_min_bishop_moves():
    solution = Solution()
    assert solution.minBishopMoves([8,1], target = [1,8]) == 1, 'wrong result'
    assert solution.minBishopMoves([4,2], target = [1,3]) == 2, 'wrong result'
    assert solution.minBishopMoves([1,1], target = [3,4]) == -1, 'wrong result'


if __name__ == '__main__':
    test_min_bishop_moves()
