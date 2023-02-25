from typing import List


class Solution:
    def maxJump(self, stones: List[int]) -> int:
        if len(stones) <= 2:
            return stones[1] - stones[0]
        res = 0
        for i in range(len(stones) - 2):
            res = max(res, stones[i + 2] - stones[i])
        return res


def test_max_jump():
    solution = Solution()
    assert solution.maxJump([0, 2, 5, 6, 7]) == 5, 'wrong result'
    assert solution.maxJump([0, 3, 9]) == 9, 'wrong result'


if __name__ == '__main__':
    test_max_jump()
