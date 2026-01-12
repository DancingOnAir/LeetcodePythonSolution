from typing import List
from collections import Counter


class Solution:
    def minGroupsForValidAssignment(self, balls: List[int]) -> int:
        cnt = Counter(balls)

        for k in range(min(cnt.values()), 0, -1):
            res = 0
            for v in cnt.values():
                q, r = divmod(v, k)
                if q < r:
                    break
                res += (v + k) // (k + 1)
            else:
                return res


def test_min_groups_for_valid_assignment():
    solution = Solution()
    assert solution.minGroupsForValidAssignment([3, 2, 3, 2, 3]) == 2, 'wrong result'
    assert solution.minGroupsForValidAssignment([10, 10, 10, 3, 1, 1]) == 4, 'wrong result'


if __name__ == '__main__':
    test_min_groups_for_valid_assignment()
