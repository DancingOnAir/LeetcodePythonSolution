from typing import List


class Solution:
    # bitmask
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        # def helper(i):

        n = len(cookies)
        m = 1 << n
        # SUM[i] 表示分配的饼干集合为i，设集合i的元素和为SUM[i]
        SUM = [0] * m
        for i, v in enumerate(cookies):
            for j in range(1 << i):
                SUM[(1 << i) | j] = SUM[j] + v

        # dp[i][mask] 表示前i个小朋友，分mask的bit位为1的糖的不平等最小值
        f = SUM.copy()
        for i in range(1, k):
            for j in range(m - 1, 0, -1):
                s = j
                while s:
                    v = f[j ^ s]
                    if SUM[s] > v:
                        v = SUM[s]
                    if v < f[j]:
                        f[j] = v
                    s = (s - 1) & j
        return f[-1]

    # backtracking
    # 优化点:
    # 1.对称重复，v[i] == 0可以避免 ？？还是不确定
    # 2.排序后从大到小遍历可以减少回溯次数
    # 3.如果回溯到剩下的还没有分配的孩子数量大于还没有分配的饼干，那么break
    # 4.如果当前已分配的孩子有饼干数目大于res，那么break
    # 5.如果有重复的，比如第一个饼干分给任一孩子都是一样的，那么只分配1次即可。同理，第二个饼干分给除了第一个已分配过的孩子外其他孩子也是一样的。
    #   i > 0 and v[i] == v[i - 1] 那么break
    def distributeCookies1(self, cookies: List[int], k: int) -> int:
        def helper(idx):
            nonlocal res
            if idx == n:
                res = min(res, max(v))
                return
            # optimization 4
            if max(v) > res:
                return
            # optimization 3
            if sum(x == 0 for x in v) > n - idx:
                return

            for i in range(k):
                # optimization 5
                if i > 0 and v[i] == v[i - 1]:
                    continue
                v[i] += cookies[idx]
                helper(idx + 1)
                v[i] -= cookies[idx]
            
        n = len(cookies)
        v = [0] * k
        # optimization 2
        cookies.sort(reverse=True)
        res = float('inf')
        helper(0)

        return res


def test_distribute_cookies():
    solution = Solution()
    assert solution.distributeCookies([8, 15, 10, 20, 8], 2) == 31, 'wrong result'
    assert solution.distributeCookies([6, 1, 3, 2, 2, 4, 1, 2], 3) == 7, 'wrong result'


if __name__ == '__main__':
    test_distribute_cookies()
