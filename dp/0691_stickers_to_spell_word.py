from typing import List
from collections import Counter


class Solution:
    def minStickers2(self, stickers: List[str], target: str) -> int:
        self.memo = {}
        stickers = [Counter(s) for s in stickers if set(s) & set(target)]

        def dfs(str):
            if not str:
                return 0

            if str in self.memo:
                return self.memo[str]

            cnt, res = Counter(str), float('inf')
            for c in stickers:
                if str[0] not in c:
                    continue
                nxt = dfs(''.join([i * j for (i, j) in (cnt - c).items()]))
                if nxt != -1:
                    res = min(res, nxt + 1)
            self.memo[str] = -1 if res == float('inf') else res
            return self.memo[str]
        return dfs(target)

    def minStickers(self, stickers: List[str], target: str) -> int:
        n = len(target)
        m = 1 << n

        dp = [0x3f3f3f3f] * m
        dp[0] = 0
        for i in range(m):
            if dp[i] == 0x3f3f3f3f:
                continue

            for sticker in stickers:
                cur = i
                for c in sticker:
                    for r in range(n):
                        if target[r] == c and not ((cur >> r) & 1):
                            cur |= 1 << r
                            break
                dp[cur] = min(dp[cur], dp[i] + 1)
        return -1 if dp[m - 1] == 0x3f3f3f3f else dp[m - 1]


def test_min_stickers():
    solution = Solution()

    assert solution.minStickers(["with", "example", "science"], "thehat") == 3, 'wrong result'
    assert solution.minStickers(["notice", "possible"], "basicbasic") == -1, 'wrong result'


if __name__ == '__main__':
    test_min_stickers()
