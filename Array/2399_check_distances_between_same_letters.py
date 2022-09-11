from typing import List


class Solution:
    # check 2nd character
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        for i, ch in enumerate(s):
            d = distance[ord(ch) - 97]
            if i + d + 1 >= len(s) or s[i + d + 1] != ch:
                return False
            # 这里distance[ord(ch) - 97] = -1，使得遇到第二个ch时，上面的i + d + 1 == i
            distance[ord(ch) - 97] = -1
        return True

    def checkDistances1(self, s: str, distance: List[int]) -> bool:
        m = dict()
        for i, ch in enumerate(s):
            if ch in m:
                if distance[ord(ch) - 97] != i - m[ch] - 1:
                    return False
            else:
                m[ch] = i
        return True


def test_check_distances():
    solution = Solution()
    assert solution.checkDistances("abaccb", [1, 3, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                              0]), 'wrong result'
    assert not solution.checkDistances("aa", [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                              0]), 'wrong result'


if __name__ == '__main__':
    test_check_distances()
