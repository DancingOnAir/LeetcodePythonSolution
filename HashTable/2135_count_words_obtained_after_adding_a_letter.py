from typing import List


class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        seen = set()
        for w in startWords:
            cur = 0
            for c in w:
                cur ^= 1 << (ord(c) - ord('a'))
            seen.add(cur)

        res = 0
        for w in targetWords:
            cur = 0
            for c in w:
                cur ^= 1 << (ord(c) - ord('a'))
            for c in w:
                if cur ^ (1 << (ord(c) - ord('a'))) in seen:
                    res += 1
                    break
        return res


def test_word_count():
    solution = Solution()

    assert solution.wordCount(["ant", "act", "tack"], ["tack", "act", "acti"]) == 2, 'wrong result'
    assert solution.wordCount(["ab", "a"], ["abc", "abcd"]) == 1, 'wrong result'


if __name__ == '__main__':
    test_word_count()

