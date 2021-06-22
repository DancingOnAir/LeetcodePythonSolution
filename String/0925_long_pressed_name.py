from itertools import groupby


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        def helper(s: str):
            return [[k, len(list(g))] for k, g in groupby(s)]

        m = helper(name)
        n = helper(typed)

        if len(m) != len(n):
            return False

        for i in range(len(m)):
            if m[i][0] != n[i][0] or m[i][1] > n[i][1]:
                return False
        return True


def test_is_long_pressed_name():
    solution = Solution()

    assert solution.isLongPressedName('leelee', 'lleeelee'), 'wrong result'
    assert solution.isLongPressedName('alex', 'aaleex'), 'wrong result'
    assert not solution.isLongPressedName('saeed', 'ssaaedd'), 'wrong result'
    assert solution.isLongPressedName('laiden', 'laiden'), 'wrong result'


if __name__ == '__main__':
    test_is_long_pressed_name()
