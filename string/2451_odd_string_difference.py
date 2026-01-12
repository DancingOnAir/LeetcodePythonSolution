from typing import List
from collections import defaultdict


class Solution:
    def oddString(self, words: List[str]) -> str:
        n = len(words[0])
        for i in range(n - 1):
            m = defaultdict(list)
            for w in words:
                m[ord(w[i + 1]) - ord(w[i])].append(w)
            if len(m) > 1:
                for k, v in m.items():
                    if len(v) == 1:
                        return v[0]
        return ''


def test_odd_string():
    solution = Solution()
    assert solution.oddString(["adc", "wzy", "abc"]) == 'abc', 'wrong result'
    assert solution.oddString(["aaa", "bob", "ccc", "ddd"]) == 'bob', 'wrong result'


if __name__ == '__main__':
    test_odd_string()
