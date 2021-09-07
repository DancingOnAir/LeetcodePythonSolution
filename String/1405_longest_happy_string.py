class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        pass


def test_longest_diverse_string():
    solution = Solution()

    assert solution.longestDiverseString(1, 1, 7) == "ccaccbcc", "wrong result"
    assert solution.longestDiverseString(2, 2, 1) == "aabbc", "wrong result"
    assert solution.longestDiverseString(7, 1, 0) == "aabaa", "wrong result"


if __name__ == '__main__':
    test_longest_diverse_string()
