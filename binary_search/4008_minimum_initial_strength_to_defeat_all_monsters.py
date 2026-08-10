from bisect import bisect_left


class Solution:
    # 二分法
    def minInitialStrength(self, monsters: list[int], boosts: list[list[int]]) -> int:
        n = len(monsters)
        bonus = [0] * (n + 1)
        for l, r, v in boosts:
            bonus[l] += v
            bonus[r + 1] -= v

        for i in range(1, n):
            bonus[i] += bonus[i - 1]

        def check(strength: int) -> bool:
            for x, b in zip(monsters, bonus):
                if strength + b < x:
                    return False
                strength = max(strength - x, 0)
            return True
        return bisect_left(range(sum(monsters)), True, key=check)

    # 差分数组
    def minInitialStrength1(self, monsters: list[int], boosts: list[list[int]]) -> int:
        n = len(monsters)
        bonus = [0] * (n + 1)
        for l, r, v in boosts:
            bonus[l] += v
            bonus[r + 1] -= v

        for i in range(1, n):
            bonus[i] += bonus[i - 1]

        res = 0
        for i in range(n - 1, -1, -1):
            if res > 0:
                res += monsters[i]
            else:
                res = max(monsters[i] - bonus[i], 0)
        return res


def test_min_initial_strength():
    solution = Solution()
    assert solution.minInitialStrength([5, 10, 15], boosts=[[1, 1, 10]]) == 30, 'wrong result'
    assert solution.minInitialStrength([5, 10, 15], boosts=[[1, 2, 10], [1, 2, 5]]) == 5, 'wrong result'


if __name__ == '__main__':
    test_min_initial_strength()
