from typing import List


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        r = mean * (len(rolls) + n) - sum(rolls)
        hist = r % n
        return [r // n] * (n - hist) + [r // n + 1] * hist

    def missingRolls1(self, rolls: List[int], mean: int, n: int) -> List[int]:
        tot = (len(rolls) + n) * mean
        tot -= sum(rolls)
        if 6 * n < tot or tot < n:
            return []

        res = []
        q, r = divmod(tot, n)
        while r:
            if q + r <= 6:
                res.append(q + r)
                break
            else:
                res.append(6)
                r -= 6 - q

        while len(res) < n:
            res.append(q)
        return res


def test_missing_rolls():
    solution = Solution()
    assert solution.missingRolls([6, 3, 4, 3, 5, 3], 1, 6) == [], 'wrong result'
    assert solution.missingRolls([3, 2, 4, 3], 4, 2) == [6, 6], 'wrong result'
    assert solution.missingRolls([1, 5, 6], 3, 4) == [3, 2, 2, 2], 'wrong result'
    assert solution.missingRolls([1, 2, 3, 4], 6, 4) == [], 'wrong result'


if __name__ == '__main__':
    test_missing_rolls()
