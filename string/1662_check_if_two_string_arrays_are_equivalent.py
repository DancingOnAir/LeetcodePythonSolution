from typing import List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        def gen(word: List[str]):
            for s in word:
                for c in s:
                    yield c
            # ensure False when len(word1) != len(word2)
            yield None

        for c1, c2 in zip(gen(word1), gen(word2)):
            if c1 != c2:
                return False
        return True

    # O(m + n)
    def arrayStringsAreEqual1(self, word1: List[str], word2: List[str]) -> bool:
        return ''.join(word1) == ''.join(word2)


def test_array_string_are_equal():
    solution = Solution()
    assert solution.arrayStringsAreEqual(["ab", "c"], ["a", "bc"]), 'wrong result'
    assert not solution.arrayStringsAreEqual(["a", "cb"], ["ab", "c"]), 'wrong result'
    assert solution.arrayStringsAreEqual(["abc", "d", "defg"], ["abcddefg"]), 'wrong result'


if __name__ == '__main__':
    test_array_string_are_equal()
