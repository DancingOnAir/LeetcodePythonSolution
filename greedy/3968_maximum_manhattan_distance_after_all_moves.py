class Solution:
    def maxDistance(self, moves: str) -> int:
        x = y = u = 0
        for m in moves:
            if m == 'U':
                y += 1
            elif m == 'D':
                y -= 1
            elif m == 'R':
                x += 1
            elif m == 'L':
                x -= 1
            else:
                u += 1
        return abs(x) + abs(y) + u


def test_max_distance():
    solution = Solution()
    assert solution.maxDistance("L_D_") == 4, 'wrong result'
    assert solution.maxDistance("U_R") == 3, 'wrong result'


if __name__ == '__main__':
    test_max_distance()
