class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        j = 0
        for i, ch in enumerate(s):
            if ch == t[j]:
                j += 1
            if j == len(t):
                return 0
        return len(t) - j


def test_append_characters():
    solution = Solution()
    assert solution.appendCharacters("coaching", "coding") == 4, 'wrong result'
    assert solution.appendCharacters("abcde", "a") == 0, 'wrong result'
    assert solution.appendCharacters("z", "abcde") == 5, 'wrong result'


if __name__ == '__main__':
    test_append_characters()
