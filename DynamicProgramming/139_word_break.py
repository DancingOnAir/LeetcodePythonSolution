from typing import List


class Solution:
    # dp[i + s1] = dp[i] & (s1 in wordDict)
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not len(s) or not len(wordDict):
            return False

        dp = [True] + [False] * len(s)

        for i in range(1, len(s) + 1):
            for j in range(0, i)[::-1]:
                dp[i] = dp[j] and (True if s[j: i] in wordDict else False)
                if dp[i]:
                    break
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
