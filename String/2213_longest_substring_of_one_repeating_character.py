from typing import List


class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        pass


def test_longest_repeating():
    solution = Solution()
    assert solution.longestRepeating('babacc', 'bcb', [1, 3, 3]) == [3, 3, 4], 'wrong result'
    assert solution.longestRepeating('abyzz', 'aa', [2, 1]) == [2, 3], 'wrong result'


if __name__ == '__main__':
    test_longest_repeating()
