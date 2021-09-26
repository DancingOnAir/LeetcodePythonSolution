class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        n = len(s)
        max_sub_seq_len = n // k

        res = list()
        for i in range(max_sub_seq_len):
            pass
        res.reverse()
        return res[0]


def test_longest_subsequence_repeated_k():
    solution = Solution()

    assert solution.longestSubsequenceRepeatedK("letsleetcode", 2) == "let", "wrong result"
    assert solution.longestSubsequenceRepeatedK("bb", 2) == "b", "wrong result"
    assert solution.longestSubsequenceRepeatedK("ab", 2) == "", "wrong result"
    assert solution.longestSubsequenceRepeatedK("bbabbabbbbabaababab", 3) == "bbbb", "wrong result"


if __name__ == '__main__':
    test_longest_subsequence_repeated_k()
