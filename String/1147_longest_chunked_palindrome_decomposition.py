class Solution:
    def longestDecomposition(self, text: str) -> int:
        res, left, right = 0, '', ''
        for i, j in zip(text, text[::-1]):
            left += i
            right = j + right

            if left == right:
                res += 1
                left, right = '', ''
        return res

    def longestDecomposition1(self, text: str) -> int:
        left, right = 0, len(text)
        i = 1
        res = 0
        while left < right:
            while text[left: left+i] != text[right - i: right]:
                i += 1

            if left + i == right:
                res += 1
            else:
                res += 2
            left += i
            right -= i
            i = 1

        return res


def test_longest_decomposition():
    solution = Solution()

    assert solution.longestDecomposition('ghiabcdefhelloadamhelloabcdefghi') == 7, 'wrong result'
    assert solution.longestDecomposition('merchant') == 1, 'wrong result'
    assert solution.longestDecomposition('antaprezatepzapreanta') == 11, 'wrong result'


if __name__ == '__main__':
    test_longest_decomposition()
