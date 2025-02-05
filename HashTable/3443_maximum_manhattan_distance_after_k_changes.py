class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        res = x = y = 0
        for i, c in enumerate(s):
            if c == 'N':
                y += 1
            elif c == 'S':
                y -= 1
            elif c == 'E':
                x += 1
            else:
                x -= 1
            res = max(res, min(i + 1, abs(x) + abs(y) + 2 * k))
        return res


def test_max_distance():
    solution = Solution()
    assert solution.maxDistance("NWSE", k=1) == 3, 'wrong result'
    assert solution.maxDistance("NSWWEW", k=3) == 6, 'wrong result'


if __name__ == '__main__':
    test_max_distance()
