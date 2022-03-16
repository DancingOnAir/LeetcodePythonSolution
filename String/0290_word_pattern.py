class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        return len(pattern) == len(s) and len(set(pattern)) == len(set(s)) == len(set(zip(pattern, s)))


def test_word_pattern():
    solution = Solution()
    assert solution.wordPattern("abba", "dog cat cat dog"), 'wrong result'
    assert not solution.wordPattern("abba", "dog cat cat fish"), 'wrong result'
    assert not solution.wordPattern("aaaa", "dog cat cat dog"), 'wrong result'


if __name__ == '__main__':
    test_word_pattern()
