from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        def shift(ch, step):
            return chr((ord(ch) - 97 + step) % 26 + 97)

        n = len(s)
        final = [0] * n
        for l, r, d in shifts:
            for i in range(l, r + 1):
                final[i] += 1 if d == 1 else -1

        res = list()
        for i, val in enumerate(final):
            res.append(shift(s[i], val))
        return ''.join(res)


def test_shifting_letters():
    solution = Solution()
    assert solution.shiftingLetters("abc", [[0, 1, 0], [1, 2, 1], [0, 2, 1]]) == "ace", 'wrong result'
    assert solution.shiftingLetters("dztz", [[0, 0, 0], [1, 1, 1]]) == "catz", 'wrong result'


if __name__ == '__main__':
    test_shifting_letters()
