from typing import List
from collections import Counter


class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        total, n = sum(skill), len(skill)
        q, r = divmod(total, n // 2)
        if r != 0:
            return -1

        skill.sort()
        left, right = 0, n - 1
        res = 0
        while left < right:
            if skill[left] + skill[right] != q:
                return -1
            res += skill[left] * skill[right]
            left += 1
            right -= 1
        return res


def test_divide_players():
    solution = Solution()
    assert solution.dividePlayers([3, 2, 5, 1, 3, 4]) == 22, 'wrong result'
    assert solution.dividePlayers([3, 4]) == 12, 'wrong result'
    assert solution.dividePlayers([1, 1, 2, 3]) == -1, 'wrong result'


if __name__ == '__main__':
    test_divide_players()
