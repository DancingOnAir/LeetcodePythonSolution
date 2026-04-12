from collections import Counter


class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        cnt = Counter(hand)
        for x in sorted(cnt):
            cur = cnt[x]
            if cur == 0:
                continue
            for y in range(x, x + groupSize):
                cnt[y] -= cur
                if cnt[y] < 0:
                    return False
        return True


def test_is_n_straight_hand():
    solution = Solution()
    assert solution.isNStraightHand([1, 2, 3, 6, 2, 3, 4, 7, 8], groupSize=3), 'wrong result'
    assert not solution.isNStraightHand([1, 2, 3, 4, 5], groupSize=4), 'wrong result'


if __name__ == '__main__':
    test_is_n_straight_hand()
