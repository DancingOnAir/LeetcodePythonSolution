from typing import List


class Solution:
    # unbound knapsack optimization
    # dp[j]: j means current target
    def largestNumber(self, cost: List[int], target: int) -> str:
        def get_bigger_str(s1, s2):
            if len(s1) < len(s2):
                return s2
            elif len(s1) > len(s2):
                return s1

            return max(s1, s2)

        dp = [''] + ['#' for _ in range(target)]
        for i in range(1, len(cost) + 1):
            for j in range(target + 1):
                if j >= cost[i - 1] and dp[j - cost[i - 1]] != '#':
                    dp[j] = get_bigger_str(dp[j], str(i) + dp[j - cost[i - 1]])

        return dp[target] if dp[target] != '#' else '0'

    # unbound knapsack
    # dp[i][j]: i means first 0..i-1 nums, j means current target
    def largestNumber2(self, cost: List[int], target: int) -> str:
        def get_bigger_str(s1, s2):
            if len(s1) < len(s2):
                return s2
            elif len(s1) > len(s2):
                return s1

            return max(s1, s2)

        n = len(cost)
        dp = [['' for _ in range(target+1)] for _ in range(n + 1)]

        for j in range(1, target + 1):
            dp[0][j] = '#'
        for i in range(1, n + 1):
            for j in range(1, target + 1):
                if j >= cost[i - 1] and dp[i][j - cost[i - 1]] != '#':
                    dp[i][j] = get_bigger_str(dp[i - 1][j], str(i) + dp[i][j - cost[i - 1]])
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[n][target] if dp[n][target] != '#' else '0'

    # TLE
    def largestNumber1(self, cost: List[int], target: int) -> str:
        def backtracking(cur: List[int], total: int) -> None:
            if total == target:
                if sorted(cur) not in nums:
                    nums.append(sorted(cur[:]))
                return

            for i in range(n):
                if target < total + cost[i]:
                    continue
                cur.append(cost[i])
                backtracking(cur, total + cost[i])
                cur.pop()

        d = dict()
        for i, val in enumerate(cost):
            d[val] = i + 1
        cost = [*d.keys()]

        n = len(cost)
        nums = list()
        backtracking([], 0)

        nums.sort(key=len, reverse=True)
        print(nums)
        if not nums:
            return '0'

        max_len = len(nums[0])
        res = ''
        for s in nums:
            if len(s) == max_len:
                res = max(res, ''.join(sorted([str(d[i]) for i in s], reverse=True)))
            else:
                break

        return res


def test_largest_number():
    solution = Solution()
    assert solution.largestNumber([4, 3, 2, 5, 6, 7, 2, 5, 5], 9) == '7772', 'wrong result'
    assert solution.largestNumber([7, 6, 5, 5, 5, 6, 8, 7, 8], 12) == '85', 'wrong result'
    assert solution.largestNumber([2, 4, 6, 2, 4, 6, 4, 4, 4], 5) == '0', 'wrong result'
    assert solution.largestNumber([6, 10, 15, 40, 40, 40, 40, 40, 40], 47) == '32211', 'wrong result'


if __name__ == '__main__':
    test_largest_number()
