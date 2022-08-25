from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        s = list(s)
        val = 0
        for i in range(len(shifts) - 1, -1, -1):
            val += shifts[i]
            s[i] = chr((ord(s[i]) - 97 + val) % 26 + 97)

        return ''.join(s)


def test_shifting_letters():
    solution = Solution()
    assert solution.shiftingLetters("abc", [3, 5, 9]) == "rpl", 'wrong result'
    assert solution.shiftingLetters("aaa", [1, 2, 3]) == "gfd", 'wrong result'


if __name__ == '__main__':
    test_shifting_letters()
