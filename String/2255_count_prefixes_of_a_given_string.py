from typing import List


class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        return sum(map(s.startswith, words))

    def countPrefixes1(self, words: List[str], s: str) -> int:
        return sum(s.startswith(w) for w in words)


def test_count_prefixes():
    solution = Solution()
    assert solution.countPrefixes(["a", "b", "c", "ab", "bc", "abc"], "abc") == 3, 'wrong result'
    assert solution.countPrefixes(["a", "a"], "aa") == 2, 'wrong result'


if __name__ == '__main__':
    test_count_prefixes()
