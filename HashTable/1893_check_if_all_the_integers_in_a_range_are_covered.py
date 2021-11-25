from typing import List


class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        cnt = 0
        for x in range(left, right + 1):
            for l, r in ranges:
                if l <= x <= r:
                    cnt += 1
                    break
        return cnt == right - left + 1

    def isCovered1(self, ranges: List[List[int]], left: int, right: int) -> bool:
        x = set(range(left, right+1))
        for r in ranges:
            x -= set(range(r[0], r[1]+1))
        return len(x) == 0


def test_is_covered():
    solution = Solution()
    assert solution.isCovered([[1, 2], [3, 4], [5, 6]], 2, 5), 'wrong result'
    assert not solution.isCovered([[1, 10], [10, 20]], 21, 21), 'wrong result'


if __name__ == '__main__':
    test_is_covered()
