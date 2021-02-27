from functools import lru_cache


class Solution:
    def rotatedDigits(self, N: int) -> int:
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
