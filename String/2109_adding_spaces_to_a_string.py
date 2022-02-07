from typing import List


class Solution:
    # forward
    def addSpaces1(self, s: str, spaces: List[int]) -> str:
        res = list()
        j = 0
        for i, ch in enumerate(s):
            if j < len(spaces) and i == spaces[j]:
                res.append(' ')
                j += 1

            res.append(ch)

        return ''.join(res)

    # backward
    def addSpaces2(self, s: str, spaces: List[int]) -> str:
        res = list()
        for i in reversed(range(len(s))):
            res.append(s[i])
            if spaces and i == spaces[-1]:
                res.append(' ')
                spaces.pop()

        return ''.join(reversed(res))

    def addSpaces(self, s: str, spaces: List[int]) -> str:
        spaces = [0] + spaces + [len(s)]
        res = list(s[spaces[i]: spaces[i + 1]] for i in range(len(spaces) - 1))
        return ' '.join(res)

def AddSpaces():
    solution = Solution()
    assert solution.addSpaces("LeetcodeHelpsMeLearn", [8, 13, 15]) == "Leetcode Helps Me Learn", 'wrong result'
    assert solution.addSpaces("icodeinpython", [1, 5, 7, 9]) == "i code in py thon", 'wrong result'
    assert solution.addSpaces("spacing", [0, 1, 2, 3, 4, 5, 6]) == " s p a c i n g", 'wrong result'


if __name__ == '__main__':
    AddSpaces()
