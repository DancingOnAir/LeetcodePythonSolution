from functools import lru_cache
from itertools import product


class Solution:
    def maxProduct(self, s: str) -> int:
        n = len(s)
        arr = list()

        for mask in range(1 << n):
            subseq = ''
            for i in range(n):
                if mask & (1 << i) > 0:
                    subseq += s[i]
            if subseq == subseq[::-1]:
                arr.append((mask, len(subseq)))

        arr.sort(key=lambda x: x[1], reverse=True)
        res = 1
        for i in range(len(arr)):
            m1, l1 = arr[i]
            if l1 ** 2 < res:
                break
            for j in range(i+1, len(arr)):
                m2, l2 = arr[j]
                if m1 & m2 == 0 and l1 * l2 > res:
                    res = l1 * l2
                    break
        return res

    def maxProduct2(self, s: str) -> int:
        n = len(s)
        arr = list()

        for mask in range(1 << n):
            subseq = ''
            for i in range(n):
                # convert mask into actual sub sequence
                if mask & (1 << i) > 0:
                    subseq += s[i]
            if subseq == subseq[::-1]:
                arr.append((mask, len(subseq)))

        res = 0
        for (m1, l1), (m2, l2) in product(arr, arr):
            # disjoint
            if m1 & m2 == 0:
                res = max(res, l1 * l2)
        return res

    # dfs but TLE
    def maxProduct1(self, s: str) -> int:
        def is_palidrome(x):
            return x == x[::-1]

        @lru_cache(None)
        def dfs(s, s1, s2, idx):
            nonlocal res
            if is_palidrome(s1) and is_palidrome(s2):
                res = max(res, len(s1) * len(s2))
            if idx == n:
                return

            dfs(s, s1+s[idx], s2, idx+1)
            dfs(s, s1, s2+s[idx], idx+1)
            dfs(s, s1, s2, idx+1)

        res = 0
        dfs(s, '', '', 0)
        return res


def test_max_product():
    solution = Solution()
    assert solution.maxProduct("leetcodecom") == 9, 'wrong result'
    assert solution.maxProduct("bb") == 1, 'wrong result'
    assert solution.maxProduct("accbcaxxcxx") == 25, 'wrong result'


if __name__ == '__main__':
    test_max_product()
