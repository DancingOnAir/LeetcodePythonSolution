class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        brokenLetters = set(brokenLetters)
        res = 0

        for w in text.split():
            if len(set(w) & brokenLetters) == 0:
                res += 1
        return res


def test_can_be_typed_words():
    solution = Solution()

    assert solution.canBeTypedWords("hello world", "ad") == 1, 'wrong result'
    assert solution.canBeTypedWords("leet code", "lt") == 1, 'wrong result'
    assert solution.canBeTypedWords("leet code", "e") == 0, 'wrong result'


if __name__ == '__main__':
    test_can_be_typed_words()
