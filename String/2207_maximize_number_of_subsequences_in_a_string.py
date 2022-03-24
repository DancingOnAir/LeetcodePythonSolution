class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        pass


def test_maximum_subsequence_count():
    solution = Solution()
    assert solution.maximumSubsequenceCount('abdcdbc', 'ac') == 4, 'wrong result'
    assert solution.maximumSubsequenceCount('aabb', 'ab') == 6, 'wrong result'


if __name__ == '__main__':
    test_maximum_subsequence_count()
