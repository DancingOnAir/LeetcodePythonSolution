from typing import List
from functools import lru_cache


class Solution:
    # top-down dp
    def longestStrChain(self, words: List[str]) -> int:
        @lru_cache(None)
        def dp(w):
            if w not in set_words:
                return 0
            return max(dp(w[:i] + w[i+1:]) for i in range(len(w))) + 1
        set_words = set(words)
        return max(dp(w) for w in words)

    # bottom-up dp
    def longestStrChain1(self, words: List[str]) -> int:
        dp = dict()
        for w in sorted(words, key=lambda x: len(x)):
            dp[w] = max(dp.get(w[: i] + w[i+1:], 0) + 1 for i in range(len(w)))
        return max(dp.values())


def test_longest_str_chain():
    solution = Solution()
    assert solution.longestStrChain(["a", "b", "ba", "bca", "bda", "bdca"]) == 4, 'wrong result'
    assert solution.longestStrChain(["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]) == 5, 'wrong result'
    assert solution.longestStrChain(["abcd", "dbqca"]) == 1, 'wrong result'


if __name__ == '__main__':
    test_longest_str_chain()
