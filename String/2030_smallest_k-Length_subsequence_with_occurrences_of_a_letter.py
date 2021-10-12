from collections import Counter


class Solution:
    def smallestSubsequence(self, s: str, k: int, letter: str, repetition: int) -> str:
        m = [[i, c] for i, c in enumerate(s)]
        m.sort(key=lambda x: x[1])

        r = k - repetition
        res = list()
        idx = 0
        while k > 0 or repetition > 0:
            if
            res.append(m[idx])
            idx += 1
            pass
        pass


def test_smallest_subsequence():
    solution = Solution()

    assert solution.smallestSubsequence("leet", 3, "e", 1) == "eet", 'wrong result'
    assert solution.smallestSubsequence("leetcode", 4, "e", 2) == "ecde", 'wrong result'
    assert solution.smallestSubsequence("bb", 2, "b", 2) == "bb", 'wrong result'


if __name__ == '__main__':
    test_smallest_subsequence()
