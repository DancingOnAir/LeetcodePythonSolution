from typing import List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return ''.join(word1) == ''.join(word2)


def test_array_string_are_equal():
    solution = Solution()
    assert solution.arrayStringsAreEqual(["ab", "c"], ["a", "bc"]), 'wrong result'
    assert not solution.arrayStringsAreEqual(["a", "cb"], ["ab", "c"]), 'wrong result'
    assert solution.arrayStringsAreEqual(["abc", "d", "defg"], ["abcddefg"]), 'wrong result'


if __name__ == '__main__':
    test_array_string_are_equal()
