class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        if n < 3:
            return False

        def dfs(first, second, i):
            if i == n:
                return True

            for j in range(i, n):
                cur = int(num[i: j + 1])
                if first == -1:
                    dfs(cur, second, j + 1)
                elif second == -1:
                    dfs(first, cur, j + 1)
                elif cur == first + second:
                    if dfs(second, cur, j + 1):
                        return True

            return False

        return dfs(-1, -1, 0)


def test_is_additive_number():
    solution = Solution()
    assert solution.isAdditiveNumber("112358"), 'wrong result'
    assert solution.isAdditiveNumber("199100199"), 'wrong result'


if __name__ == '__main__':
    test_is_additive_number()
