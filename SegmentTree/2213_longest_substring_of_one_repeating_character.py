from typing import List
from itertools import groupby
from functools import lru_cache


class Node:
    def __init__(self):
        self.left, self.right = None, None
        # 表示区间的左边下标和右边下标
        self.l, self.r = 0, 0
        # 表示区间内最左边的字符和最右边的字符
        self.lch, self.rch = None, None
        # 表示该区间的字符串中，前缀重复的长度和后缀重复的长度
        self.pre, self.suf = 0, 0
        # 表示该区间最长的连续重复的子字符串长度
        self.most = 0

    def merge(self):
        if not self.left:
            return
        # 更新pre
        if self.left.lch == self.right.lch and self.left.pre == self.left.r - self.left.l + 1:
            self.lch = self.left.lch
            self.pre = self.left.pre + self.right.pre
        else:
            self.lch = self.left.lch
            self.pre = self.left.pre

        # 更新suf
        if self.left.rch == self.right.rch and self.right.suf == self.right.r - self.right.l + 1:
            self.rch = self.right.rch
            self.suf = self.left.suf + self.right.suf
        else:
            self.rch = self.right.rch
            self.suf = self.right.suf

        # 更新most
        self.most = max(self.left.most, self.right.most)
        if self.left.rch == self.right.lch:
            self.most = max(self.most, self.left.suf + self.right.pre)

    @classmethod
    def build(cls, s, l, r):
        cur = cls()
        cur.l, cur.r = l, r
        if l == r:
            cur.lch, cur.rch = s[l], s[r]
            cur.pre = cur.suf = 1
            cur.most = 1
        else:
            mid = (l + r) >> 1
            cur.left = cls.build(s, l, mid)
            cur.right = cls.build(s, mid + 1, r)
            cur.merge()
        return cur

    def update(self, idx, ch):
        if self.l == self.r:
            self.lch = self.rch = ch
            return

        mid = (self.l + self.r) >> 1
        if idx <= mid:
            self.left.update(idx, ch)
        else:
            self.right.update(idx, ch)
        self.merge()


class Solution:
    def __init__(self):
        self.s = None
        # L[i]表示在节点i管理的区域中，从左侧延伸的单字母长度
        self.L = [0] * 400005
        # R[i]表示在节点i管理的区域中，从右侧延伸的单字母长度
        self.R = [0] * 400005
        # A[i]表示在节点i管理的区域中，单字母的最大长度
        self.A = [0] * 400000

    def merge(self, node, l, r):
        nl = node << 1
        nr = nl | 1
        mid = (l + r) >> 1
        self.A[node] = max(self.A[nl], self.A[nr])
        self.L[node] = self.L[nl]
        self.R[node] = self.R[nr]
        if self.s[mid] == self.s[mid + 1]:
            self.A[node] = max(self.A[node], self.R[nl] + self.L[nr])
            if self.A[nl] == mid - l + 1:
                self.L[node] += self.L[nr]
            if self.A[nr] == r - mid:
                self.R[node] += self.R[nl]

    def build(self, node, l, r):
        if l == r:
            self.L[node] = self.R[node] = self.A[node] = 1
        else:
            mid = (l + r) >> 1
            self.build(node << 1, l, mid)
            self.build((node << 1) | 1, mid + 1, r)
            self.merge(node, l, r)

    def query(self, node, l, r, i, c):
        if l == r:
            self.s[l] = c
        else:
            mid = (l + r) >> 1
            if i <= mid:
                self.query(node << 1, l, mid, i, c)
            else:
                self.query((node << 1) | 1, mid + 1, r, i, c)
            self.merge(node, l, r)
        return self.A[node]

    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        self.s = list(s)
        self.build(1, 0, len(s) - 1)

        res = list()
        for ch, idx in zip(queryCharacters, queryIndices):
            res.append(self.query(1, 0, len(s) - 1, idx, ch))
        return res

    # segment tree
    def longestRepeating2(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        st = Node.build(s, 0, len(s) - 1)
        res = list()
        for ch, idx in zip(queryCharacters, queryIndices):
            st.update(idx, ch)
            res.append(st.most)
        return res

    # TLE
    def longestRepeating1(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        @lru_cache(None)
        def helper(ss):
            return max(len(list(g)) for _, g in groupby(ss))

        s = list(s)
        res = list()
        for i, val in enumerate(queryIndices):
            s[val] = queryCharacters[i]
            x = helper(''.join(s))
            res.append(x)
        return res


def test_longest_repeating():
    solution = Solution()
    assert solution.longestRepeating('babacc', 'bcb', [1, 3, 3]) == [3, 3, 4], 'wrong result'
    assert solution.longestRepeating('abyzz', 'aa', [2, 1]) == [2, 3], 'wrong result'


if __name__ == '__main__':
    test_longest_repeating()
