from typing import List
from functools import lru_cache


class Solution:
    def getWordsInLongestSubsequence(self, n: int, words: List[str], groups: List[int]) -> List[str]:
        res = []
        path = []

        def dfs(i, pre):
            nonlocal res
            if len(path) > len(res):
                res = path.copy()

            if i >= n:
                return

            if groups[i] != pre:
                path.append(words[i])
                dfs(i + 1, groups[i])
                path.pop()
            else:
                dfs(i + 1, pre)

        dfs(0, -1)
        return res


def test_get_words_in_longest_subsequence():
    solution = Solution()
    assert solution.getWordsInLongestSubsequence(3, ["e", "a", "b"], [0, 0, 1]) == ["a", "b"], 'wrong result'
    assert solution.getWordsInLongestSubsequence(4, ["a", "b", "c", "d"], [1, 0, 1, 1]) == ["a", "b",
                                                                                            "d"], 'wrong result'


if __name__ == '__main__':
    test_get_words_in_longest_subsequence()

