from typing import List


class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        i = 0
        for w in words:
            j = i + len(w)
            if s[i: j] != w:
                return False
            if j == len(s):
                return True
            i = j

        return False


def test_is_prefix_string():
    solution = Solution()
    assert solution.isPrefixString("iloveleetcode", ["i", "love", "leetcode", "apples"]), 'wrong result'
    assert not solution.isPrefixString("iloveleetcode", ["apples", "i", "love", "leetcode"]), 'wrong result'


if __name__ == '__main__':
    test_is_prefix_string()

