from math import ceil, sqrt


class Solution:
    # math
    def canAliceWin(self, n: int) -> bool:
        x = (21 - ceil(sqrt(441 - n * 8))) // 2
        return x % 2 > 0

    # simulation
    def canAliceWin1(self, n: int) -> bool:
        pick = 10
        while pick <= n:
            n -= pick
            pick -= 1
        return (pick - 1) % 2 == 0


def test_can_alice_win():
    solution = Solution()
    assert solution.canAliceWin(12), 'wrong result'
    assert not solution.canAliceWin(1), 'wrong result'


if __name__ == '__main__':
    test_can_alice_win()
