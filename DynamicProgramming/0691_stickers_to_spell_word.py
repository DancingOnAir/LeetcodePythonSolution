from typing import List
from collections import Counter


class Solution:
    # def minStickers(self, stickers: 'List[str]', target: 'str') -> 'int':
    #     stickers, self.map = [Counter(s) for s in stickers if set(s) & set(target)], {}
    #     def dfs(target):
    #         if not target: return 0
    #         if target in self.map: return self.map[target]
    #         cnt, res = Counter(target), float('inf')
    #         for c in stickers: # traverse the stickers to get new target
    #             if c[target[0]] == 0: continue # we can make sure the 1st letter will be removed to reduce the time complexity
    #             nxt = dfs(''.join([s * t for (s, t) in (cnt - c).items()]))
    #             if nxt != -1: res = min(res, 1 + nxt)
    #         self.map[target] = -1 if res == float('inf') else res
    #         return self.map[target]
    #     return dfs(target)

    def minStickers(self, stickers: List[str], target: str) -> int:
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

    def minStickers1(self, stickers: List[str], target: str) -> int:
        # n = len(target)
        # m = 1 << n
        #
        # dp = [0x3f3f3f3f] * m
        # dp[0] = 0
        # for i in range(m):
        #     if dp[i] == -1:
        #         continue
        #
        #     for sticker in stickers:
        #         now = i
        #         for c in sticker:
        #             for r in range(n):
        #                 if target[r] == c and ~((now >> r) & 1):
        #                     now |= 1 << r
        #                     break
        #         dp[now] = min(dp[now], dp[i] + 1)
        #
        # return dp[m - 1]
        pass


def test_min_stickers():
    solution = Solution()

    assert solution.minStickers(["with", "example", "science"], "thehat") == 3, 'wrong result'
    assert solution.minStickers(["notice", "possible"], "basicbasic") == -1, 'wrong result'


if __name__ == '__main__':
    test_min_stickers()
