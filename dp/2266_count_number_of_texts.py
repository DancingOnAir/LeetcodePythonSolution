from itertools import groupby
from functools import reduce, lru_cache
from operator import mul


class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        @lru_cache(None)
        def helper(x, i):
            if i == 0 or i == 1:
                return 1

            ans = 0
            for j in range(1, m[x] + 1):
                if i < j:
                    break
                ans += helper(x, i - j)
                ans %= mod
            return ans

        mod = 10 ** 9 + 7
        m = {'2': 3, '3': 3, '4': 3, '5': 3, '6': 3, '7': 4, '8': 3, '9': 4}
        res = []
        for k, g in groupby(pressedKeys):
            res.append(helper(k, len(list(g))))
        return reduce(mul, res) % mod


def test_count_texts():
    solution = Solution()
    assert solution.countTexts("22233") == 8, 'wrong result'
    assert solution.countTexts("222222222222222222222222222222222222") == 82876089, 'wrong result'


if __name__ == '__main__':
    test_count_texts()
