class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        l = len(str(n))
        res = 0
        cnt = [0] * 10

        def dfs(i, x):
            if i == l:
                if x <= n or any(i != v for i, v in enumerate(cnt) if v != 0):
                    return False
                nonlocal res
                res = x
                return True

            for j in range(1, l + 1):
                if cnt[j] >= j:
                    continue

                cnt[j] += 1
                if dfs(i + 1, x * 10 + j):
                    return True
                cnt[j] -= 1
            return False

        # n <= 10 ** 6
        while l < 8:
            if dfs(0, 0):
                break
            l += 1
        return res


def test_next_beautiful_number():
    solution = Solution()
    assert solution.nextBeautifulNumber(748601) == 1224444, 'wrong result'
    assert solution.nextBeautifulNumber(1) == 22, 'wrong result'
    assert solution.nextBeautifulNumber(1000) == 1333, 'wrong result'
    assert solution.nextBeautifulNumber(3000) == 3133, 'wrong result'


if __name__ == '__main__':
    test_next_beautiful_number()
