from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        res, last = 0, float('-inf')
        for s, e in sorted(pairs, key=lambda x: x[1]):
            if s > last:
                res += 1
                last = e
        return res

    def findLongestChain(self, pairs: List[List[int]]) -> int:
        n = len(pairs)
        if n < 2:
            return n

        pairs.sort()
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if pairs[j][1] < pairs[i][0] and dp[i] <= dp[j]:
                    dp[i] = dp[j] + 1
        return dp[n - 1]


def test_find_longest_chain():
    solution = Solution()

    pairs1 = [[1, 2], [2, 3], [3, 4]]
    # pairs1 = [[2, 3], [3, 4], [1, 2], [2, 5]]
    assert solution.findLongestChain(pairs1) == 2, 'wrong result'


if __name__ == '__main__':
    test_find_longest_chain()
