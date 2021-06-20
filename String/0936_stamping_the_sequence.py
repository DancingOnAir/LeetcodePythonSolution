from typing import List


class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
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
    assert solution.movesToStamp('uskh', 'uskhkhhskh') == [5, 4, 6, 3, 1, 2, 0], 'wrong result'
    assert solution.movesToStamp('abc', 'ababc') == [0, 2], 'wrong result'
    assert solution.movesToStamp('abca', 'aabcaca') == [3, 0, 1], 'wrong result'


if __name__ == '__main__':
    test_moves_to_stamp()
