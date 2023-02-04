from typing import List


class Solution:
    # backtracking
    # 优化点:
    # 1.对称重复，v[i] == 0可以避免 ？？还是不确定
    # 2.排序后从大到小遍历可以减少回溯次数
    # 3.如果回溯到剩下的还没有分配的孩子数量大于还没有分配的饼干，那么break
    # 4.如果当前已分配的孩子有饼干数目大于res，那么break
    # 5.如果有重复的，比如第一个饼干分给任一孩子都是一样的，那么只分配1次即可。同理，第二个饼干分给除了第一个已分配过的孩子外其他孩子也是一样的。
    #   i > 0 and v[i] == v[i - 1] 那么break
    def distributeCookies(self, cookies: List[int], k: int) -> int:
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
