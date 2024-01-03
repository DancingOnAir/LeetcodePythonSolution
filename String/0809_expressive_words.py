from typing import List
from collections import Counter
from itertools import groupby


class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def check(s1, s2):
            i, j, n, m = 0, 0, len(s1), len(s2)
            for i in range(n):
                if j < m and s1[i] == s2[j]:
                    j += 1
                elif s[i - 2: i + 1] != s[i] * 3 != s[i - 1: i + 2]:
                    return False

            return j == m

        return sum(check(s, w) for w in words)

    def expressiveWords1(self, s: str, words: List[str]) -> int:
        def helper(w):
            return [(k, len(list(g))) for k, g in groupby(w)]

        m = helper(s)
        res = 0
        for w in words:
            cur = helper(w)
            if len(cur) != len(m):
                continue

            for i in range(len(m)):
                if cur[i][0] != m[i][0] or m[i][1] < cur[i][1] or cur[i][1] < m[i][1] < 3:
                    break
            else:
                res += 1
        return res


def test_expressive_words():
    solution = Solution()
    assert solution.expressiveWords("sass", ["sa"]) == 0, 'wrong result'
    assert solution.expressiveWords("abcd", ["abc"]) == 0, 'wrong result'
    assert solution.expressiveWords("heeellooo", ["hello", "hi", "helo"]) == 1, 'wrong result'
    assert solution.expressiveWords("zzzzzyyyyy", ["zzyy","zy","zyy"]) == 3, 'wrong result'


if __name__ == '__main__':
    test_expressive_words()
