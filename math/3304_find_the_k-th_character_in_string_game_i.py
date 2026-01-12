from math import floor, log


class Solution:
    def kthCharacter(self, k: int) -> str:
        s = 'a'
        while k > len(s):
            s += ''.join(chr((ord(c) - ord('a') + 1) % 26 + 97) for c in s)
        return s[k - 1]


def test_kth_character():
    solution = Solution()
    assert solution.kthCharacter(5) == 'b', 'wrong result'
    assert solution.kthCharacter(10) == 'c', 'wrong result'


if __name__ == '__main__':
    test_kth_character()
