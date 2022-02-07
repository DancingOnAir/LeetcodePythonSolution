from typing import List


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        pass


def test_add_spaces():
    solution = Solution()
    assert solution.addSpaces("LeetcodeHelpsMeLearn", [8,13,15]) == "Leetcode Helps Me Learn", 'wrong result'
    assert solution.addSpaces("icodeinpython", [1,5,7,9]) == "i code in py thon", 'wrong result'
    assert solution.addSpaces("spacing", [0,1,2,3,4,5,6]) == " s p a c i n g", 'wrong result'


if __name__ == '__main__':
    test_add_spaces()
