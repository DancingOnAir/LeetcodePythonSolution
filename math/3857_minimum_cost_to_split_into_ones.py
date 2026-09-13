class Solution:
    def minCost1(self, n: int) -> int:
        return n * (n + 1) // 2

    def minCost1(self, n: int) -> int:
        def dfs(x):
            if x == 1:
                return 1

            a = x // 2
            b = x - a

            res = a * b
            if a > 1:
                res += dfs(a)
            if b > 1:
                res += dfs(b)
            return res
        return dfs(n) if n > 1 else 0

def test_min_cost():
    solution = Solution()
    assert solution.minCost(3) == 3, 'wrong result'
    assert solution.minCost(4) == 6, 'wrong result'


if __name__ == '__main__':
    test_min_cost()
