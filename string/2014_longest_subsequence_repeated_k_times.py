from collections import Counter
from itertools import permutations


class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        freq = Counter(s)
        hot = ''.join(ele * (freq[ele] // k) for ele in sorted(freq, reverse=True))
        for i in range(len(hot), 0, -1):
            for item in permutations(hot, i):
                word = ''.join(item)
                # 巧妙运用iter来遍历整个s
                ss = iter(s)
                if all(c in ss for c in word * k):
                    return word
        return ''


def test_longest_subsequence_repeated_k():
    solution = Solution()

    assert solution.longestSubsequenceRepeatedK("letsleetcode", 2) == "let", "wrong result"
    assert solution.longestSubsequenceRepeatedK("bb", 2) == "b", "wrong result"
    assert solution.longestSubsequenceRepeatedK("ab", 2) == "", "wrong result"
    assert solution.longestSubsequenceRepeatedK("bbabbabbbbabaababab", 3) == "bbbb", "wrong result"


if __name__ == '__main__':
    test_longest_subsequence_repeated_k()
