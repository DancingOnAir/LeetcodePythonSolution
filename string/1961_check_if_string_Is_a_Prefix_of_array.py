from typing import List


class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        return not len(s) or (words and s.startswith(words[0]) and self.isPrefixString(s[len(words[0]):], words[1:]))

    def isPrefixString1(self, s: str, words: List[str]) -> bool:
        i = 0
        for w in words:
            if s[i: i + len(w)] != w:
                return False
            i += len(w)
            if i == len(s):
                return True
        return False


def test_is_prefix_string():
    solution = Solution()
    assert solution.isPrefixString("iloveleetcode", ["i", "love", "leetcode", "apples"]), 'wrong result'
    assert not solution.isPrefixString("iloveleetcode", ["apples", "i", "love", "leetcode"]), 'wrong result'


if __name__ == '__main__':
    test_is_prefix_string()

