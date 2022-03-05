class Solution:
    def countVowels(self, word: str) -> int:
        pass


def test_count_vowels():
    solution = Solution()
    assert solution.countVowels('aba') == 6, 'wrong result'
    assert solution.countVowels('abc') == 3, 'wrong result'
    assert solution.countVowels('ltcd') == 0, 'wrong result'


if __name__ == '__main__':
    test_count_vowels()
