from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not len(s) or not len(wordDict):
            return False

        dp = [True] + [False] * len(s)
        for i in range(1, len(s) + 1):
            for w in wordDict:
                l = len(w)
                if l <= i and w == s[i - l: i]:
                    dp[i] = dp[i] or dp[i - l]
        return dp[-1]

    def wordBreak1(self, s: str, wordDict: List[str]) -> bool:
        if not len(s) or not len(wordDict):
            return False

        dp = [True] + [False] * len(s)
        max_len = max([len(x) for x in wordDict])
        min_len = min([len(x) for x in wordDict])

        for i in range(0, len(s) + 1):
            for j in range(min_len, max_len + 1):
                if i + j > len(s):
                    break

                if dp[i] and (s[i: i + j] in wordDict):
                    dp[i + j] = True
        return dp[len(s)]


def test_word_break():
    solution = Solution()

    s1 = "leetcode"
    wordDict1 = ["leet", "code"]
    assert solution.wordBreak(s1, wordDict1), "wrong result"

    s2 = "applepenapple"
    wordDict2 = ["apple", "pen"]
    assert solution.wordBreak(s2, wordDict2), "wrong result"

    s3 = "catsandog"
    wordDict3 = ["cats", "dog", "sand", "and", "cat"]
    assert not solution.wordBreak(s3, wordDict3), "wrong result"


if __name__ == '__main__':
    test_word_break()
