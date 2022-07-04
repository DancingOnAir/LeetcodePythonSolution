from typing import List
from math import comb
from collections import defaultdict


class Solution:
    # 用到的数论知识
    # 1.欧拉函数(Euler's totient function), 对于正整数n, 欧拉函数是小于等于n的正整数中与n互质的数的数目,记做φ(n) eg. φ(1)=1，φ(8)=4
    # 2.费马小定理, 互质的2个正整数a和n，有a^φ(n) ≡ 1 (mod n)
    # 3.特别的, 如果正整数n为质数，那么φ(n) = n - 1, 则有a^(n - 1) ≡ 1 (mod n)
    # 4.该题用到的技巧:
    #   a.  2个正整数a，b和取模用的质数m = 10 ** 9 + 7 求 (a^b) % m
    #       这里m为质数,那么φ(m) = m - 1 = 10 ** 9 + 6, 假设b = k * 1_000_000_006 + r (k, r均为整数，k是商，r是余数)
    #       那么 (a^b) % m = (a^(k * 1_000_000_006 + r)) % m = ((a^1_000_000_006)^k) % m * (a^r) % m = (a^r) % m
    #   b.  乘法逆元，正整数a，存在另一个正整数b (0 < b < m), 满足 (a*b) % m = 1, 则称b为a的逆元
    #       如何求b，利用费马小定理 a^(m - 1) ≡ 1 (mod m), 有a^(m - 1) * b ≡ b, 可以推出a^(m - 2) * (a * b) ≡ b, 即a^(m - 2) ≡ b
    # https://leetcode.com/problems/count-ways-to-build-rooms-in-an-ant-colony/discuss/1299540/PythonC%2B%2B-clean-DFS-solution-with-explanation
    def waysToBuildRooms(self, prevRoom: List[int]) -> int:
        mod = 10 ** 9 + 7
        n = len(prevRoom)
        # fac是阶乘，inv是乘法逆元
        fac, inv = [0] * n, [0] * n
        fac[0] = inv[0] = 1
        for i in range(1, n):
            fac[i] = fac[i - 1] * i % mod
            inv[i] = pow(fac[i], mod - 2, mod)

        # 构造图
        edges = defaultdict(list)
        for i, node in enumerate(prevRoom):
            edges[node].append(i)
        # f[i]表示以节点i为根的子树的拓扑排序方案数
        # cnt[i]表示以节点i为根的子树中节点的个数
        f, cnt = [0] * n, [0] * n

        def dfs(u):
            f[u] = 1
            for v in edges[u]:
                dfs(v)
                f[u] = f[u] * f[v] * inv[cnt[v]] % mod
                cnt[u] += cnt[v]
            f[u] = f[u] * fac[cnt[u]] % mod
            cnt[u] += 1

        dfs(0)
        return f[0]

    def waysToBuildRooms1(self, prevRoom: List[int]) -> int:
        connect = defaultdict(list)
        for i, num in enumerate(prevRoom):
            connect[num].append(i)

        def dfs(idx):
            l, res = 0, 1
            for child in connect[idx]:
                r, tmp = dfs(child)
                res = (res * comb(l + r, r) * tmp) % (10 ** 9 + 7)
                l += r
            return l + 1, res
        return dfs(0)[1]


def test_ways_to_build_rooms():
    solution = Solution()
    assert solution.waysToBuildRooms([-1, 0, 1]) == 1, 'wrong result'
    assert solution.waysToBuildRooms([-1, 0, 0, 1, 2]) == 6, 'wrong result'


if __name__ == '__main__':
    test_ways_to_build_rooms()
