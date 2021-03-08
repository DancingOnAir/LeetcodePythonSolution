class Solution:
    # brute force solution
    def checkPartitioning(self, s: str) -> bool:
        n = len(s)
        # split string s into 3 parts: s[:left], s[left, right], s[:right]
        for i in range(1, n - 1):
            if s[:i] == s[:i][::-1]:
                for j in range(i + 1, n):
                    if s[i:j] == s[i:j][::-1] and s[j:] == s[j:][::-1]:
                        return True
        return False


def test_check_partitioning():
    solution = Solution()
    assert solution.checkPartitioning('abcbdd'), 'wrong result'
    assert not solution.checkPartitioning('bcbddxy'), 'wrong result'
    assert solution.checkPartitioning('bbab'), 'wrong result'


if __name__ == '__main__':
    test_check_partitioning()
