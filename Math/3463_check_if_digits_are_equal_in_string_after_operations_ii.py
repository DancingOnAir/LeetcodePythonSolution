from itertools import pairwise
from math import pow


MOD = 10
mx = 100_000
f = [1] + [0] * mx
inv_f = [0] * (1 + mx)
p2 = [0] * (1 + mx)
p5 = [0] * (1 + mx)

for i in range(1, mx + 1):
    x = i
    # x&-x计算x二进制最后一个1的代表的数，比如12 = (1100)，最后一个1代表的数是(100) = 4
    # 这里计算二进制下x尾部有多少0，即包含多少个2的因子
    e2 = (x & -x).bit_length() - 1
    x >>= e2
    e5 = 0
    while x % 5 == 0:
        e5 += 1
        x //= 5
    f[i] = f[i - 1] * x % MOD
    p2[i] = p2[i - 1] + e2
    p5[i] = p5[i - 1] + e5
# 欧拉定理求逆元，欧拉公式10为3
inv_f[mx] = pow(f[mx], 3, MOD)
for i in range(mx, 0, -1):
    x = i
    x >>= (x & -x).bit_length() - 1
    while x % 5 == 0:
        x //= 5
    inv_f[i - 1] = inv_f[i] * x % MOD


def comb(n, k):
    return f[n] * inv_f[n - k] * inv_f[k] * pow(2, p2[n] - p2[k] - p2[n - k], MOD) * pow(5, p5[n] - p5[k] - p5[n - k], MOD)


class Solution:
    def hasSameDigits(self, s: str) -> bool:
        n = len(s)
        s = map(ord, s)
        return sum(comb(n - 2, i) * (x - y) for i, (x, y) in enumerate(pairwise(s))) % 10 == 0


def test_has_same_digits():
    solution = Solution()
    assert solution.hasSameDigits("3902"), 'wrong result'
    assert not solution.hasSameDigits("34789"), 'wrong result'


if __name__ == '__main__':
    test_has_same_digits()
