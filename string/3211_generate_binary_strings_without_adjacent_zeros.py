from typing import List


class Solution:
    def validStrings(self, n: int) -> List[str]:
        res = [0, 1]
        for _ in range(n - 1):
            tmp = []
            for x in res:
                if x & 1:
                    tmp.append(2 * x)
                tmp.append(2 * x + 1)
            res = tmp

        return [bin(x)[2:].rjust(n, '0') for x in res]

    def validStrings1(self, n: int) -> List[str]:
        def dfs(x, pre, s):
            nonlocal res
            if x == 0:
                res.append(s)
                return

            if x == 1:
                if pre != "10":
                    res.append(s + "0")
                res.append(s + "1")
                return

            if pre != "10":
                dfs(x - 2, "01", s + "01")
            dfs(x - 2, "10", s + "10")
            dfs(x - 2, "11", s + "11")

        res = []
        dfs(n, "", "")
        return res


def test_valid_strings():
    solution = Solution()
    assert solution.validStrings(3) == ["010", "011", "101", "110", "111"], 'wrong result'
    assert solution.validStrings(1) == ["0", "1"], 'wrong result'


if __name__ == '__main__':
    test_valid_strings()

