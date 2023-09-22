class Solution:
    # backtracking
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        res = '9' * (n + 1)
        path = []

        def dfs(i):
            if i == n + 1:
                nonlocal res
                res = min(res, ''.join(path))
                return

            for j in range(1, 10):
                if str(j) in path:
                    continue

                if i == 0 or (pattern[i - 1] == 'I' and str(j) > path[-1]) or (pattern[i - 1] == 'D' and str(j) < path[-1]):
                    path.append(str(j))
                    dfs(i + 1)
                    path.pop()
        dfs(0)
        return res

    # greed
    def smallestNumber1(self, pattern: str) -> str:
        n = len(pattern)
        res = [str(i) for i in range(1, n + 2)]

        i, j = 0, 0
        while i < n:
            if pattern[i] == 'I':
                i += 1
                j += 1
            else:
                cnt = 0
                while i < n and pattern[i] == 'D':
                    i += 1
                    cnt += 1
                res[j: j + cnt + 1] = res[j: j + cnt + 1][::-1]
                j = i

        return ''.join(res)


def test_smallest_number():
    solution = Solution()
    assert solution.smallestNumber("IIIDIDDD") == "123549876", 'wrong result'
    assert solution.smallestNumber("DDD") == "4321", "wrong result"


if __name__ == '__main__':
    test_smallest_number()
