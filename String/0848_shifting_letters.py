from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        res = list()
        shift = 0
        for i in range(len(s) - 1, -1, -1):
            shift += shifts[i]
            res.append(chr((ord(s[i]) - ord('a') + shift) % 26 + ord('a')))
        return ''.join(res[::-1])


def test_shifting_letters():
    solution = Solution()
    assert solution.shiftingLetters('abc', [3, 5, 9]) == 'rpl'
    assert solution.shiftingLetters('aaa', [1, 2, 3]) == 'gfd'


if __name__ == '__main__':
    test_shifting_letters()
