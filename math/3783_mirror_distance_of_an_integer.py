class Solution:
    def mirrorDistance(self, n: int) -> int:
        return abs(int(''.join(str(n)[::-1])) - n)


def test_mirror_distance():
    solution = Solution()
    assert solution.mirrorDistance(25) == 27, 'wrong result'
    assert solution.mirrorDistance(10) == 9, 'wrong result'
    assert solution.mirrorDistance(7) == 0, 'wrong result'


if __name__ == '__main__':
    test_mirror_distance()
