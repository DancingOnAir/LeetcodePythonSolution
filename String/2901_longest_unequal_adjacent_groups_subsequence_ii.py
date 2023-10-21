from typing import List


class Solution:
    # dp
    def getWordsInLongestSubsequence(self, n: int, words: List[str], groups: List[int]) -> List[str]:
        def hamming_dist(s1, s2):
            return len(s1) == len(s2) and sum(c1 != c2 for c1, c2 in zip(s1, s2)) == 1

        dp = [0] * n
        from_dp = [0] * n
        mx = n - 1

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if dp[j] > dp[i] and groups[j] != groups[i] and hamming_dist(words[j], words[i]):
                    dp[i] = dp[j]
                    from_dp[i] = j

            dp[i] += 1
            if dp[i] > dp[mx]:
                mx = i

        res = [''] * dp[mx]
        for i in range(dp[mx]):
            res[i] = words[mx]
            mx = from_dp[mx]
        return res

    # backtracking
    def getWordsInLongestSubsequence1(self, n: int, words: List[str], groups: List[int]) -> List[str]:
        res = []
        path = []

        def hamming_dist(s1, s2):
            return len(s1) == len(s2) and sum(c1 != c2 for c1, c2 in zip(s1, s2)) == 1

        def dfs(i, pre):
            if i == n:
                nonlocal res
                if len(path) > len(res):
                    res = path.copy()
                return

            dfs(i + 1, pre)
            if groups[i] != pre and (not path or hamming_dist(path[-1], words[i])):
                path.append(words[i])
                dfs(i + 1, groups[i])
                path.pop()

        dfs(0, -1)
        return res


def test_get_words_in_longest_subsequence():
    solution = Solution()
    assert solution.getWordsInLongestSubsequence(4, ["cbb", "db", "bdd", "bd"], [2, 3, 4, 3]) == ["bd"], 'wrong result'
    assert solution.getWordsInLongestSubsequence(3, ["bab", "dab", "cab"], [1, 2, 2]) == ["bab", "cab"], 'wrong result'
    assert solution.getWordsInLongestSubsequence(4, ["a", "b", "c", "d"], [1, 2, 3, 4]) == ["a", "b", "c",
                                                                                            "d"], 'wrong result'


if __name__ == '__main__':
    test_get_words_in_longest_subsequence()
