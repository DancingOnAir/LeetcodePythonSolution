from typing import List


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        n = len(matchsticks)
        if n < 4:
            return False

        tot = sum(matchsticks)
        if tot % 4:
            return False
        target = tot // 4
        sides = [0] * 4
        matchsticks.sort(reverse=True)

        def dfs(i):
            if i == n:
                return True

            for j in range(4):
                if j > 0 and sides[j - 1] == sides[j]:
                    continue

                if sides[j] + matchsticks[i] <= target:
                    sides[j] += matchsticks[i]
                    if dfs(i + 1):
                        return True
                    sides[j] -= matchsticks[i]
                    if sides[j] == 0:
                        break
            return False
        return dfs(0)


def test_make_square():
    solution = Solution()
    assert solution.makesquare([1, 1, 2, 2, 2]), 'wrong result'
    assert not solution.makesquare([3, 3, 3, 3, 4]), 'wrong result'


if __name__ == '__main__':
    test_make_square()
