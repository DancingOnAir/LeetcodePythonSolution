from typing import List


class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def devowel(s: str) -> str:
            res = ''
            vowels = set('aeiou')
            for i, c in enumerate(s):
                if c in vowels:
                    res += '*'
                else:
                    res += c
            return res

        def helper(s: str) -> str:
            if s in word_prefect:
                return s
            if s.lower() in word_lower:
                return word_lower[s.lower()]
            if devowel(s.lower()) in word_vowel:
                return word_vowel[devowel(s.lower())]
            return ''

        word_prefect = set(wordlist)
        word_lower = dict()
        word_vowel = dict()
        for w in wordlist:
            word_lower.setdefault(w.lower(), w)
            word_vowel.setdefault(devowel(w.lower()), w)

        return list(map(helper, queries))


def test_spell_checker():
    solution = Solution()
    assert solution.spellchecker(["ae", "aa"], ["UU"]) == ["ae"], 'wrong result'
    assert solution.spellchecker(["KiTe", "kite", "hare", "Hare"],
                                 ["kite", "Kite", "KiTe", "Hare", "HARE", "Hear", "hear", "keti", "keet", "keto"]) == [
               "kite", "KiTe", "KiTe", "Hare", "hare", "", "", "KiTe", "", "KiTe"], 'wrong result'
    assert solution.spellchecker(["yellow"], ["YellOw"]) == ["yellow"], 'wrong result'


if __name__ == '__main__':
    test_spell_checker()
