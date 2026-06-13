class Solution:
    def generateValidStrings(self, n: int, k: int) -> list[str]:
        res = []
        cur = []


        def dfs(idx: int, cost: int, pre_is_one: bool) -> None:
            if cost > k:
                return
            if idx == n:
                res.append("".join(cur))
                return

            cur.append('0')
            dfs(idx+1, cost, False)
            cur.pop()

            if not pre_is_one and cost + idx <= k:
                cur.append('1')
                dfs(idx+1, cost + idx, True)
                cur.pop()

        dfs(0, 0, False)
        return res


def test_generate_valid_strings():
    solution = Solution()
    assert solution.generateValidStrings(3, 1) == ["000","010","100"]
    assert solution.generateValidStrings(1, 0) == ["0","1"]


if __name__ == '__main__':
    test_generate_valid_strings()
