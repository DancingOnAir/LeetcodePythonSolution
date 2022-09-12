from typing import List
from collections import defaultdict, Counter


class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if len(set(suits)) == 1:
            return "Flush"

        if Counter(ranks).most_common(1)[0][1] >= 3:
            return "Three of a Kind"
        if Counter(ranks).most_common(1)[0][1] == 2:
            return "Pair"
        return "High Card"

    # straight forward
    def bestHand1(self, ranks: List[int], suits: List[str]) -> str:
        res = ["Flush", "Three of a Kind", "Pair", "High Card"]
        if len(set(suits)) == 1:
            return res[0]

        freq = max(v for _, v in Counter(ranks).items())
        if freq >= 3:
            return res[1]
        if freq == 2:
            return res[2]
        return res[3]


def test_best_hand():
    solution = Solution()
    assert solution.bestHand([13, 2, 3, 1, 9], ["a", "a", "a", "a", "a"]) == "Flush", 'wrong result'
    assert solution.bestHand([4, 4, 2, 4, 4], ["d", "a", "a", "b", "c"]) == "Three of a Kind", 'wrong result'


if __name__ == '__main__':
    test_best_hand()
