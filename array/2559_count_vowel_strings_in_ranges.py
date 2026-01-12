from typing import List


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowel = {'a', 'e', 'i', 'o', 'u'}
        pre_sum = [0]
        for w in words:
            pre_sum.append(pre_sum[-1] + (1 if w[0] in vowel and w[-1] in vowel else 0))

        res = list()
        for l, r in queries:
            res.append(pre_sum[r + 1] - pre_sum[l])
        return res


def test_vowel_strings():
    solution = Solution()
    assert solution.vowelStrings(["aba", "bcb", "ece", "aa", "e"], [[0, 2], [1, 4], [1, 1]]) == [2, 3,
                                                                                                 0], 'wrong result'
    assert solution.vowelStrings(["a", "e", "i"], [[0, 2], [0, 1], [2, 2]]) == [3, 2, 1], 'wrong result'


if __name__ == '__main__':
    test_vowel_strings()
