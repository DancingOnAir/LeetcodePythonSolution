from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums * 2


def test_get_concatenation():
    solution = Solution()
    assert solution.getConcatenation([1, 2, 1]) == [1, 2, 1, 1, 2, 1], 'wrong result'
    assert solution.getConcatenation([1, 3, 2, 1]) == [1, 3, 2, 1, 1, 3, 2, 1], 'wrong result'


if __name__ == '__main__':
    test_get_concatenation()
