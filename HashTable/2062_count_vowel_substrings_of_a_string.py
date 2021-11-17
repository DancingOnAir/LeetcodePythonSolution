from collections import defaultdict


class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        res = 0
        last_consonant = -1
        vowels = {c: -1 for c in 'aeiou'}

        for i, c in enumerate(word):
            if c in vowels:
                vowels[c] = i
                res += max(min(vowels.values()) - last_consonant, 0)
            else:
                last_consonant = i

        return res

    def countVowelSubstrings1(self, word: str) -> int:
        freq = defaultdict(int)
        res = j = 0
        for i, c in enumerate(word):
            if c in 'aeiou':
                if not i or word[i - 1] not in 'aeiou':
                    jj = j = i
                    freq.clear()

                freq[c] += 1
                while len(freq) == 5 and all(freq.values()):
                    freq[word[j]] -= 1
                    j += 1
                res += j - jj

        return res


def test_count_vowel_substrings():
    solution = Solution()
    assert solution.countVowelSubstrings("aaeiouu") == 4, 'wrong result'
    assert solution.countVowelSubstrings("unicornarihan") == 0, 'wrong result'
    assert solution.countVowelSubstrings("cuaieuouac") == 7, 'wrong result'
    assert solution.countVowelSubstrings("bbaeixoubb") == 0, 'wrong result'


if __name__ == '__main__':
    test_count_vowel_substrings()
