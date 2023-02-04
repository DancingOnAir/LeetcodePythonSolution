from typing import List


class Solution:
    # backtracking
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        def helper(idx):
            if idx == n:
                nonlocal res
                res = min(res, max(v))
                return
            for i in range(k):
                v[i] += cookies[idx]
                helper(idx + 1)
                v[i] -= cookies[idx]
                if v[i] == 0:
                    break
            
        n = len(cookies)
        v = [0] * k
        res = float('inf')
        helper(0)

        return res


def test_distribute_cookies():
    solution = Solution()
    assert solution.distributeCookies([8, 15, 10, 20, 8], 2) == 31, 'wrong result'
    assert solution.distributeCookies([6, 1, 3, 2, 2, 4, 1, 2], 3) == 7, 'wrong result'


if __name__ == '__main__':
    test_distribute_cookies()
