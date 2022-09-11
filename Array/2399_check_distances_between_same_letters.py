from typing import List


class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
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
