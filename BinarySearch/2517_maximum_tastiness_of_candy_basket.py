from typing import List


class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()

        def check(dist):
            cnt, x = 1, price[0]
            for p in price:
                if p >= x + dist:
                    x = p
                    cnt += 1
            return cnt >= k

        left, right = 0, (price[-1] - price[0]) // (k - 1)
        while left <= right:
            mid = left + (right - left) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid - 1
        return left - 1


def test_maximum_tastiness():
    solution = Solution()
    assert solution.maximumTastiness([13, 5, 1, 8, 21, 2], 3) == 8, 'wrong result'
    assert solution.maximumTastiness([1, 3, 1], 2) == 2, 'wrong result'
    assert solution.maximumTastiness([7, 7, 7, 7], 2) == 0, 'wrong result'


if __name__ == '__main__':
    test_maximum_tastiness()
