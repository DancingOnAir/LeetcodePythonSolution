from typing import List


class Solution:
    # bit manipulate + math
    # https://leetcode.cn/problems/find-products-of-elements-of-big-array/solutions/2774549/olog-shi-tian-fa-pythonjavacgo-by-endles-w2l4/
    def findProductsOfElements(self, queries: List[List[int]]) -> List[int]:
        def sum_e(k):
            res, n, cnt1, sum_i = 0, 0, 0, 0
            for i in range((k + 1).bit_length() - 1, 0, -1):
                # 新增幂次个数
                c = (cnt1 << i) + (i << (i - 1))
                if c <= k:
                    k -= c
                    # 新增幂次和
                    res += (sum_i << i) + ((i * (i - 1) // 2) << (i - 1))
                    # 之前1的幂次之和
                    sum_i += i
                    # 之前bit位1的个数
                    cnt1 += 1
                    # 试填法形成的数
                    n |= 1 << i
            # 最低位单独计算
            if cnt1 <= k:
                k -= cnt1
                res += sum_i
                n += 1
            # 剩余的 k 个幂次，由 n 的低 k 个 1 补充
            for _ in range(k):
                lb = n & -n
                res += lb.bit_length() - 1
                n ^= lb
            return res
        return [pow(2, sum_e(r + 1) - sum_e(l), mod) for l, r, mod in queries]

    # TLE
    def findProductsOfElements1(self, queries: List[List[int]]) -> List[int]:
        ps = [0]
        mx = max(q[1] for q in queries)
        for i in range(1, 2 ** mx + 1):
            for j, b in enumerate(bin(i)[2:][::-1]):
                if b == '1':
                    ps.append(ps[-1] + j)
        res = []
        for x, y, mod in queries:
            res.append(pow(2, ps[y + 1] - ps[x], mod))
        return res


def test_find_products_of_elements():
    solution = Solution()
    assert solution.findProductsOfElements([[0, 1, 1]]) == [0], 'wrong result'
    assert solution.findProductsOfElements([[1, 3, 7]]) == [4], 'wrong result'
    assert solution.findProductsOfElements([[2, 5, 3], [7, 7, 4]]) == [2, 2], 'wrong result'


if __name__ == '__main__':
    test_find_products_of_elements()
