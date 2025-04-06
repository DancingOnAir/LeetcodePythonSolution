from math import sqrt, isclose


class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        def dist(x, y):
            return sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2)

        def blocked(attacker, blocker, queen):
            return isclose(dist(attacker, blocker) + dist(blocker, queen), dist(attacker, queen))

        if (a == e or b == f) and not blocked((a, b), (c, d), (e, f)):
            return 1
        if abs(c - e) == abs(d - f) and not blocked((c, d), (a, b), (e, f)):
            return 1
        return 2


def test_min_moves_to_capture_the_queen():
    solution = Solution()
    assert solution.minMovesToCaptureTheQueen(1, b=1, c=8, d=8, e=2, f=3) == 2, 'wrong result'
    assert solution.minMovesToCaptureTheQueen(5, b=3, c=3, d=4, e=5, f=2) == 1, 'wrong result'


if __name__ == '__main__':
    test_min_moves_to_capture_the_queen()
