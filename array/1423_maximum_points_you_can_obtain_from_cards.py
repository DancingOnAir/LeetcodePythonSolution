from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        res = cur = sum(cardPoints[:k])
        for i in range(k-1, -1, -1):
            cur = cur - cardPoints[i] + cardPoints[i - k]
            res = max(res, cur)

        return res

    def maxScore2(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        if k >= n:
            return sum(cardPoints)

        res, left, count, total = float('inf'), 0, 0, 0
        for right in range(n):
            total += cardPoints[right]
            count += 1

            if count > n - k:
                total -= cardPoints[left]
                left += 1
                count -= 1

            if count == n - k:
                res = min(res, total)

        return sum(cardPoints) - res

    def maxScore1(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        if k >= n:
            return sum(cardPoints)

        new_card_points = cardPoints[-k:] + cardPoints[:k]
        res = 0
        left, count, total = 0, 0, 0
        for right in range(2*k):
            total += new_card_points[right]
            count += 1

            if count > k:
                total -= new_card_points[left]
                count -= 1
                left += 1

            if count == k:
                res = max(res, total)

        return res


def test_max_score():
    solution = Solution()

    cardPoints1 = [1, 2, 3, 4, 5, 6, 1]
    k1 = 3
    print(solution.maxScore(cardPoints1, k1))

    cardPoints2 = [2, 2, 2]
    k2 = 2
    print(solution.maxScore(cardPoints2, k2))

    cardPoints3 = [9, 7, 7, 9, 7, 7, 9]
    k3 = 7
    print(solution.maxScore(cardPoints3, k3))

    cardPoints4 = [1, 1000, 1]
    k4 = 1
    print(solution.maxScore(cardPoints4, k4))

    cardPoints5 = [1, 79, 80, 1, 1, 1, 200, 1]
    k5 = 3
    print(solution.maxScore(cardPoints5, k5))

    cardPoints6 = [100, 40, 17, 9, 73, 75]
    k6 = 3
    print(solution.maxScore(cardPoints6, k6))


if __name__ == '__main__':
    test_max_score()
