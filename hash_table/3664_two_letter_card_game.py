from typing import List, Dict, Tuple
from collections import Counter


class Solution:
    def calc(self, cnt: Dict[str, int]) -> Tuple[int, int]:
        sum_cnt = sum(cnt.values())
        max_cnt = max(cnt.values(), default=0)
        pairs = min(sum_cnt // 2, sum_cnt - max_cnt)
        return pairs, sum_cnt - pairs * 2

    def score(self, cards: List[str], x: str) -> int:
        cnt = Counter(cards)
        cnt_xx = cnt.pop(x + x, 0)
        cnt1 = {b: c for (a, b), c in cnt.items() if a == x}
        cnt2 = {a: c for (a, b), c in cnt.items() if b == x}

        pair1, left1 = self.calc(cnt1)
        pair2, left2 = self.calc(cnt2)
        res = pair1 + pair2

        if cnt_xx > 0:
            mn = min(cnt_xx, left1 + left2)
            res += mn
            cnt_xx -= mn

        if cnt_xx > 0:
            res += min(cnt_xx // 2, pair1 + pair2)

        return res


def test_score():
    solution = Solution()
    assert solution.score(["aa","ab","ba","ac"], x = "a") == 2, 'wrong result'
    assert solution.score(["aa","ab","ba"], x = "a") == 1, 'wrong result'
    assert solution.score(["aa","ab","ba","ac"], x = "b") == 0, 'wrong result'


if __name__ == '__main__':
    test_score()
