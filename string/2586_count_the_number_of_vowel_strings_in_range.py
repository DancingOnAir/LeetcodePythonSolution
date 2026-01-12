from typing import List


class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        return sum(words[i][0] in 'aeiou' and words[i][-1] in 'aeiou' for i in range(left, right + 1))


def test_vowel_strings():
    solution = Solution()
    assert solution.vowelStrings(["are", "amy", "u"], 0, 2) == 2, 'wrong result'
    assert solution.vowelStrings(["hey", "aeo", "mu", "ooo", "artro"], 1, 4) == 3, 'wrong result'


if __name__ == '__main__':
    test_vowel_strings()
