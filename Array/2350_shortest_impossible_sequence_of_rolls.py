from typing import List


class Solution:
    # https://leetcode.cn/problems/shortest-impossible-sequence-of-rolls/solution/nao-jin-ji-zhuan-wan-tan-xin-shi-zhao-zh-j8hd/
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        s = set()
        res = 0
        for val in rolls:
            s.add(val)
            if len(s) == k:
                s.clear()
                res += 1
        return res + 1


def test_shortest_sequence():
    solution = Solution()
    assert solution.shortestSequence([3, 3, 4, 5, 2, 1, 1, 5], 5) == 2, 'wrong result'
    assert solution.shortestSequence([4, 2, 1, 2, 3, 3, 2, 4, 1], 4) == 3, 'wrong result'
    assert solution.shortestSequence([1, 1, 2, 2], 2) == 2, 'wrong result'
    assert solution.shortestSequence([1, 1, 3, 2, 2, 2, 3, 3], 4) == 1, 'wrong result'


if __name__ == '__main__':
    test_shortest_sequence()
