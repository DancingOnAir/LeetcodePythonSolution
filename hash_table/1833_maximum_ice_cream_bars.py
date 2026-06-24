from collections import Counter


class Solution:
    # O(n + U) U = max(costs)
    def maxIceCream(self, costs: list[int], coins: int) -> int:
        mx = max(costs)
        m = [0] * (mx + 1)
        for cost in costs:
            m[cost] += 1

        res = 0
        for cost in range(1, mx + 1):
            if coins < cost:
                break
            cnt = min(coins // cost, m[cost])
            res += cnt
            coins -= cnt * cost

        return res

    # O(nlog(n))
    def maxIceCream1(self, costs: list[int], coins: int) -> int:
        cnt = Counter(costs)
        res = 0
        for cost in sorted(cnt):
            cur = cost * cnt[cost]
            if coins >= cur:
                res += cnt[cost]
                coins -= cur
            else:
                res += coins // cost
                break
        return res


def test_max_ice_cream():
    solution = Solution()
    assert solution.maxIceCream([1,3,2,4,1], coins = 7) == 4, 'wrong result'
    assert solution.maxIceCream([10,6,8,7,7,8], coins = 5) == 0, 'wrong result'
    assert solution.maxIceCream([1,6,3,1,2,5], coins = 20) == 6, 'wrong result'


if __name__ == '__main__':
    test_max_ice_cream()



