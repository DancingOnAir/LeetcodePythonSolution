class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        if n > 24:
            return (n - 24) * 4 + 48
        elif n > 16:
            return (n - 16) * 3 + 24
        elif n > 8:
            return (n - 8) * 2 + 8
        return n


def test_minimum_pushes():
    solution = Solution()
    assert solution.minimumPushes("abcde") == 5, 'wrong result'
    assert solution.minimumPushes("xycdefghij") == 12, 'wrong result'


if __name__ == '__main__':
    test_minimum_pushes()
