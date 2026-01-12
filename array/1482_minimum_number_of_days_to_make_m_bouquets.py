from typing import List


class Solution:
    # binary search
    # ref: https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/discuss/769703/Python-Clear-explanation-Powerful-Ultimate-Binary-Search-Template.-Solved-many-problems.
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def validate(days):
            bonquets, flowers = 0, 0
            for bloom in bloomDay:
                if bloom > days:
                    flowers = 0
                else:
                    bonquets += (flowers + 1) // k
                    flowers = (flowers + 1) % k
            return bonquets >= m

        if m * k > len(bloomDay):
            return -1

        left, right = 1, max(bloomDay)
        while left < right:
            mid = left + (right - left) // 2
            if validate(mid):
                right = mid
            else:
                left = mid + 1

        return left


def test_min_days():
    solution = Solution()

    bloomDay1 = [1, 10, 3, 10, 2]
    m1 = 3
    k1 = 1
    print(solution.minDays(bloomDay1, m1, k1))

    bloomDay2 = [1, 10, 3, 10, 2]
    m2 = 3
    k2 = 2
    print(solution.minDays(bloomDay2, m2, k2))

    bloomDay3 = [7, 7, 7, 7, 12, 7, 7]
    m3 = 2
    k3 = 3
    print(solution.minDays(bloomDay3, m3, k3))

    bloomDay4 = [1000000000, 1000000000]
    m4 = 1
    k4 = 1
    print(solution.minDays(bloomDay4, m4, k4))

    bloomDay5 = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]
    m5 = 4
    k5 = 2
    print(solution.minDays(bloomDay5, m5, k5))


if __name__ == '__main__':
    test_min_days()
