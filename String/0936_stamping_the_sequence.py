from typing import List
from collections import defaultdict


class Solution:
    # dfs
    def movesToStamp(self, stamp, target):
        if stamp[0] != target[0] or stamp[-1] != target[-1]:
            return []

        n, m = len(stamp), len(target)
        path = [0] * m
        pos = defaultdict(set)
        for i, c in enumerate(stamp):
            pos[c].add(i)

        def dfs(i, idx):
            path[i] = idx
            if i == m - 1:
                return idx == n - 1
            nxt_idx = set()

            if idx == n - 1:
                nxt_idx |= pos[target[i + 1]]
            elif stamp[idx + 1] == target[i + 1]:
                nxt_idx.add(idx + 1)
            if stamp[0] == target[i + 1]:
                nxt_idx.add(0)

            return any(dfs(i + 1, j) for j in nxt_idx)

        def path2res(path):
            down, up = list(), list()
            for i in range(len(path)):
                if path[i] == 0:
                    up.append(i)
                elif i and path[i] - 1 != path[i - 1]:
                    down.append(i - path[i])
            return down[::-1] + up

        if not dfs(0, 0):
            return []
        return path2res(path)

    # greedy solution
    def movesToStamp2(self, stamp, target):
        n, m, t, s, res = len(target), len(stamp), list(target), list(stamp), list()

        def check(i):
            changed = False
            for j in range(m):
                if t[i + j] == '?':
                    continue
                if t[i + j] != s[j]:
                    return False
                changed = True
            if changed:
                t[i: i+m] = ['?'] * m
                res.append(i)
            return changed

        changed = True
        while changed:
            changed = False
            for i in range(n - m + 1):
                changed |= check(i)
        return res[::-1] if t == ['?'] * n else []

    # failed solution
    def movesToStamp1(self, stamp: str, target: str) -> List[int]:
        res = list()
        n = len(stamp)
        mask = '?' * n

        def helper(s, t):
            while True:
                pos = t.find(s)
                if pos == -1:
                    break
                res.append(pos)
                t = t.replace(s, mask, 1)
            return t

        target = helper(stamp, target)

        i = 1
        while i < n:
            cur = stamp[0: n - i] + '?' * i
            new_target = helper(cur, target)
            if new_target != target:
                target = new_target
                i = 1
            else:
                i += 1

        i = 1
        while i < n:
            cur = '?' * i + stamp[i:]
            new_target = helper(cur, target)
            if new_target != target:
                target = new_target
                i = 1
            else:
                i += 1

        if target != '?' * len(target):
            return list()

        res.reverse()
        return res


def test_moves_to_stamp():
    solution = Solution()
    # assert solution.movesToStamp('uskh', 'uskhkhhskh') == [5, 4, 6, 3, 1, 2, 0], 'wrong result'
    assert solution.movesToStamp('abc', 'ababc') == [0, 2], 'wrong result'
    assert solution.movesToStamp('abca', 'aabcaca') == [3, 0, 1], 'wrong result'


if __name__ == '__main__':
    test_moves_to_stamp()
