from typing import List
from bisect import bisect_left


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(scores)
        dp = [0] * n
        arr = sorted(zip(scores, ages))
        for i, (score, age) in enumerate(arr):
            for j in range(n):
                if arr[j][1] <= age:
                    dp[i] = max(dp[i], dp[j])
            dp[i] += score
        return max(dp)


def test_beast_team_score():
    solution = Solution()
    assert solution.bestTeamScore([1, 3, 5, 10, 15], [1, 2, 3, 4, 5]) == 34, 'wrong result'
    assert solution.bestTeamScore([4, 5, 6, 5], [2, 1, 2, 1]) == 16, 'wrong result'
    assert solution.bestTeamScore([1, 2, 3, 5], [8, 9, 10, 1]) == 6, 'wrong result'


if __name__ == '__main__':
    test_beast_team_score()
