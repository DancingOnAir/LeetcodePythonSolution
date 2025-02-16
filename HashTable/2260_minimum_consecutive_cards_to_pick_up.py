from typing import List
from collections import defaultdict


class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        cnt = defaultdict(list)
        res = float('inf')
        for i, x in enumerate(cards):
            cnt[x].append(i)
            if len(cnt[x]) > 1:
                res = min(res, cnt[x][-1] - cnt[x][-2] + 1)
        return res if res < float('inf') else -1


def test_minimum_card_pickup():
    solution = Solution()
    assert solution.minimumCardPickup([3, 4, 2, 3, 4, 7]) == 4, 'wrong result'
    assert solution.minimumCardPickup([1, 0, 5, 3]) == -1, 'wrong result'


if __name__ == '__main__':
    test_minimum_card_pickup()
