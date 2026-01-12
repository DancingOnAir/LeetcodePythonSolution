from typing import List
from string import ascii_lowercase


class Solution:
    def stringSequence(self, target: str) -> List[str]:
        res = []
        for t in target:
            pre = res[-1] if res else ''
            for i in range(ord(t) - ord('a') + 1):
                res.append(pre + ascii_lowercase[i])
        return res


def test_string_sequence():
    solution = Solution()
    assert solution.stringSequence("abc") == ["a", "aa", "ab", "aba", "abb", "abc"], 'wrong result'
    assert solution.stringSequence("he") == ["a", "b", "c", "d", "e", "f", "g", "h", "ha", "hb", "hc", "hd",
                                             "he"], 'wrong result'


if __name__ == '__main__':
    test_string_sequence()
