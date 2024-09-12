class Solution:
    def doesAliceWin(self, s: str) -> bool:
        return sum(1 if c in {'a', 'e', 'i', 'o', 'u'} else 0 for c in s) > 0


def test_does_alice_win():
    solution = Solution()
    assert solution.doesAliceWin("leetcoder"), 'wrong result'
    assert not solution.doesAliceWin("bbcd"), 'wrong result'


if __name__ == '__main__':
    test_does_alice_win()
