from typing import List


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def helper(a: str, b: str):
            return b.startswith(a) and b.endswith(a)

        n, res = len(words), 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                if helper(words[i], words[j]):
                    res += 1

        return res


def test_count_prefix_suffix_paris():
    solution = Solution()
    assert solution.countPrefixSuffixPairs(["a", "aba", "ababa", "aa"]) == 4, 'wrong result'
    assert solution.countPrefixSuffixPairs(["pa", "papa", "ma", "mama"]) == 2, 'wrong result'


if __name__ == '__main__':
    test_count_prefix_suffix_paris()
