from typing import List


class Solution:
    def maximumCoins(self, coins: List[List[int]], k: int) -> int:
        def helper(nums, sz):
            res = left = cover = 0
            for l, r, c in nums:
                cover += (r - l + 1) * c
                while nums[left][1] < r - sz + 1:
                    cover -= (nums[left][1] - nums[left][0] + 1) * nums[left][2]
                    left += 1
                uncover = max(0, r - sz + 1 - nums[left][0]) * nums[left][2]
                res = max(res, cover - uncover)
            return res

        coins.sort()
        ans = helper(coins, k)
        coins.reverse()
        for i in range(len(coins)):
            coins[i][0], coins[i][1] = -coins[i][1], -coins[i][0]
        return max(ans, helper(coins, k))


def test_maximum_coins():
    solution = Solution()
    assert solution.maximumCoins([[8, 10, 1], [1, 3, 2], [5, 6, 4]], 4) == 10, 'wrong result'
    assert solution.maximumCoins([[1, 10, 3]], 2) == 6, 'wrong result'


if __name__ == '__main__':
    test_maximum_coins()
