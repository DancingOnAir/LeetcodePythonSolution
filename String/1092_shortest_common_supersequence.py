class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        pass


def test_shortest_common_supersequence():
    solution = Solution()

    assert solution.shortestCommonSupersequence('abac', 'cab') == 'cabac', 'wrong result'
    assert solution.shortestCommonSupersequence('aaaaaaaa', 'aaaaaaaa') == 'aaaaaaaa', 'wrong result'


if __name__ == '__main__':
    test_shortest_common_supersequence()
