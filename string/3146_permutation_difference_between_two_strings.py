class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        m = dict()
        for i, c in enumerate(s):
            m[c] = i

        res = 0
        for i, c in enumerate(t):
            res += abs(m[c] - i)
        return res


def test_find_permutation_difference():
    solution = Solution()
    assert solution.findPermutationDifference("abc", "bac") == 2, 'wrong result'
    assert solution.findPermutationDifference("abcde", "edbac") == 12, 'wrong result'


if __name__ == '__main__':
    test_find_permutation_difference()
