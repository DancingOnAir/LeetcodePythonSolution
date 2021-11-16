from collections import defaultdict


class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        m = defaultdict(int)
        res = i = 0
        for j in range(len(word)):
            if word[j] in 'aeiou':
                m[word[j]] += 1
                if len(m) == 5:
                    res += 1
            else:
                i += 1
                while word[i] in 'aeiou':
                    m[word[i]] -= 1
                    if m[word[i]] == 0:
                        del m[word[i]]
                    if len(m) == 5:
                        res += 1
                i = j

        return res


def test_count_vowel_substrings():
    solution = Solution()
    assert solution.countVowelSubstrings("aeiouu") == 2, 'wrong result'
    assert solution.countVowelSubstrings("unicornarihan") == 0, 'wrong result'
    assert solution.countVowelSubstrings("cuaieuouac") == 7, 'wrong result'
    assert solution.countVowelSubstrings("bbaeixoubb") == 0, 'wrong result'