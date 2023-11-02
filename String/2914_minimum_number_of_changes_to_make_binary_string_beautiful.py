class Solution:
    def minChanges(self, s: str) -> int:
        return sum(s[i] != s[i + 1] for i in range(0, len(s), 2))


def test_min_changes():
    solution = Solution()
    assert solution.minChanges("1001") == 2, 'wrong result'
    assert solution.minChanges("10") == 1, 'wrong result'
    assert solution.minChanges("0000") == 0, 'wrong result'


if __name__ == '__main__':
    test_min_changes()
