class Solution:
    def longestDecomposition(self, text: str) -> int:
        pass


def test_longest_decomposition():
    solution = Solution()
    assert solution.longestDecomposition('ghiabcdefhelloadamhelloabcdefghi') == 7, 'wrong result'
    assert solution.longestDecomposition('merchant') == 1, 'wrong result'
    assert solution.longestDecomposition('antaprezatepzapreanta') == 11, 'wrong result'


if __name__ == '__main__':
    test_longest_decomposition()
