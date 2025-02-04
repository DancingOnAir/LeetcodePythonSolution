from typing import List


class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n, m = len(word1), len(word2)
        last = [-1] * m
        j = m - 1
        for i in range(n - 1, -1, -1):
            if j >= 0 and word1[i] == word2[j]:
                last[j] = i
                j -= 1

        res = []
        skip = j = 0
        for i, c in enumerate(word1):
            if j == m:
                break
            if c == word2[j] or (skip == 0 and (j == m - 1 or i < last[j + 1])):
                skip += c != word2[j]
                res.append(i)
                j += 1
        return res if j == m else []


def test_valid_sequence():
    solution = Solution()
    assert solution.validSequence("vbcca", word2="abc") == [0, 1, 2], 'wrong result'
    assert solution.validSequence("bacdc", word2="abc") == [1, 2, 4], 'wrong result'
    assert solution.validSequence("aaaaaa", word2="aaabc") == [], 'wrong result'
    assert solution.validSequence("abc", word2="ab") == [0, 1], 'wrong result'


if __name__ == '__main__':
    test_valid_sequence()
