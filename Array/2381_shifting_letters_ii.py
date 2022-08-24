from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        pass


def test_shifting_letters():
    solution = Solution()
    assert solution.shiftingLetters("abc", [[0, 1, 0], [1, 2, 1], [0, 2, 1]]) == "ace", 'wrong result'
    assert solution.shiftingLetters("dztz", [[0, 0, 0], [1, 1, 1]]) == "catz", 'wrong result'


if __name__ == '__main__':
    test_shifting_letters()
