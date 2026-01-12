from functools import lru_cache


class Solution:
    # dp
    # if digit in [3, 4, 7], then dp[i] = -1
    # if it's in [0, 1, 8], dp[i] = 0
    # if it's in [2, 5, 6, 9], dp[i] = 1
    def rotatedDigits(self, N: int) -> int:
        dp = [0, 0, 1, -1, -1, 1, 1, -1, 0, 1] + [0] * (N - 9)
        for i in range(1, N+1):
            if dp[i // 10] == -1 or dp[i % 10] == -1:
                dp[i] = -1
            elif dp[i // 10] == 1 and dp[i % 10] == 1:
                dp[i] = 1
        # 不能dp.count(1), 如果N < 9，需要截取
        return dp[:N + 1].count(1)

    # brute force
    def rotatedDigits2(self, N: int) -> int:
        res = 0
        for i in range(1, N+1):
            s = str(i)

            res += (all(d not in '347' for d in s) and any(d in '2569' for d in s))
        return res

    # digit dp
    def rotatedDigits1(self, N: int) -> int:
        N = list(map(int, str(N)))
        non_rotatings = [0, 1, 8]
        rotatings = [2, 5, 6, 9]

        @lru_cache(None)
        def dp(idx, prefix, bigger, has_rotating):
            if idx == len(N):
                return 0

            res = 0
            for i in range(1 if not idx else 0, 10):
                if i not in rotatings and i not in non_rotatings:
                    continue

                _prefix = prefix and i == N[idx]
                _bigger = bigger or (prefix and i > N[idx])
                _has_rotating = has_rotating or (i in rotatings)

                if _has_rotating and not (idx == len(N) - 1 and _bigger):
                    res += 1
                res += dp(idx + 1, _prefix, _bigger, _has_rotating)
            return res

        return dp(0, True, False, False)


def test_rotated_digits():
    solution = Solution()
    assert solution.rotatedDigits(10) == 4, 'wrong result'


if __name__ == '__main__':
    test_rotated_digits()
