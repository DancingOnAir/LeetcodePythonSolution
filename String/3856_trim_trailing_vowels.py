class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        for i in range(len(s) - 1, -1, -1):
            if s[i] not in {'a', 'e', 'i', 'o', 'u'}:
                return s[:i + 1]
        return ""


def test_trim_trailing_vowels():
    solution = Solution()
    assert solution.trimTrailingVowels("idea") == "id", 'wrong result'
    assert solution.trimTrailingVowels("day") == "day", 'wrong result'
    assert solution.trimTrailingVowels("aeiou") == "", 'wrong result'


if __name__ == '__main__':
    test_trim_trailing_vowels()
