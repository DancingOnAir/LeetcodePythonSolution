from string import ascii_lowercase


class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        vowels = consonant = 0
        for c in s:
            if c in ascii_lowercase:
                if c in 'aeiou':
                    vowels += 1
                else:
                    consonant += 1
        return (vowels // consonant) if consonant > 0 else 0


def test_vowel_consonant_score():
    solution = Solution()
    assert solution.vowelConsonantScore("cooear") == 2, 'wrong result'
    assert solution.vowelConsonantScore("axeyizou") == 1, 'wrong result'
    assert solution.vowelConsonantScore("au 123") == 0, 'wrong result'


if __name__ == '__main__':
    test_vowel_consonant_score()

