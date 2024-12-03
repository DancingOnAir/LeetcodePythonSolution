class Solution:
    def canAliceWin(self, n: int) -> bool:
        cnt = 10
        while cnt <= n:
            n -= cnt
            cnt -= 1
        return (cnt - 1) % 2 == 0


def test_can_alice_win():
    solution = Solution()
    assert solution.canAliceWin(12), 'wrong result'
    assert not solution.canAliceWin(1), 'wrong result'


if __name__ == '__main__':
    test_can_alice_win()
