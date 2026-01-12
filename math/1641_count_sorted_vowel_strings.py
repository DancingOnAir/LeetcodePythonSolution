from math import comb


class Solution:
    def countVowelStrings(self, n: int) -> int:
        return comb(n + 4, 4) % (10 ** 9 + 7)


def test_count_vowel_strings():
    solution = Solution()
    assert solution.countVowelStrings(1) == 5, 'wrong result'
    assert solution.countVowelStrings(2) == 15, 'wrong result'
    assert solution.countVowelStrings(33) == 66045, 'wrong result'


if __name__ == '__main__':
    test_count_vowel_strings()
