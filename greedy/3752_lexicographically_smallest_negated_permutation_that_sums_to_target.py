from typing import List


class Solution:
    def lexSmallestNegatedPerm(self, n: int, target: int) -> List[int]:
        tot = (1 + n) * n // 2
        if abs(target) > tot or (tot - target) % 2:
            return []

        res = [0] * n
        neg_s = (tot - target) // 2
        l, r = 0, n - 1
        for x in range(n, 0, -1):
            if neg_s >= x:
                neg_s -= x
                res[l] = -x
                l += 1
            else:
                res[r] = x
                r -= 1
        return res


def test_lex_smallest_negated_perm():
    solution = Solution()
    assert solution.lexSmallestNegatedPerm(1, -1) == [-1], 'wrong result'
    assert solution.lexSmallestNegatedPerm(3, 0) == [-3, 1, 2], 'wrong result'
    assert solution.lexSmallestNegatedPerm(1, 10000000000) == [], 'wrong result'


if __name__ == '__main__':
    test_lex_smallest_negated_perm()
