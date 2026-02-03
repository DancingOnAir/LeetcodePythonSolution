from typing import List


class Solution:
    def minTime(self, s: str, order: List[int], k: int) -> int:
        n = len(s)
        cnt = n * (n - 1) // 2
        if cnt < k:
            return -1

        pre = list(range(-1, n))
        nxt = list(range(1, n + 2))

        for t in range(n - 1, -1, -1):
            i = order[t]
            l, r = pre[i], nxt[i]
            cnt -= (i - l) * (r - i)
            if cnt < k:
                return t
            nxt[l] = r
            pre[r] = l

        return -1


def test_min_time():
    solution = Solution()
    assert solution.minTime("abc", order=[1, 0, 2], k=2) == 0, 'wrong result'
    assert solution.minTime("cat", order=[0, 2, 1], k=6) == 6, 'wrong result'
    assert solution.minTime("xy", order=[0, 1], k=4) == -1, 'wrong result'


if __name__ == '__main__':
    test_min_time()
