from typing import List


class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        res = []
        x = 0

        def dfs(i):
            nonlocal x
            if i == n:
                res.append(x)
                return

            if i == 0:
                for j in range(1, 10):
                    x = j
                    dfs(i + 1)
            else:
                cur = x
                last_digit = x % 10
                if last_digit - k >= 0:
                    x = x * 10 + last_digit - k
                    dfs(i + 1)
                    x = cur

                if last_digit + k < 10:
                    x = x * 10 + last_digit + k
                    dfs(i + 1)
                    x = cur
        dfs(0)
        return res


def test_nums_same_consec_diff():
    solution = Solution()
    assert solution.numsSameConsecDiff(3, 7) == [181, 292, 707, 818, 929], 'wrong result'
    assert solution.numsSameConsecDiff(2, 1) == [10, 12, 21, 23, 32, 34, 43, 45, 54, 56, 65, 67, 76, 78, 87, 89,
                                                 98], 'wrong result'


if __name__ == '__main__':
    test_nums_same_consec_diff()
