from collections import Counter
from heapq import heappop, heappush, heapify


class Solution:
    # https://leetcode.com/problems/reorganize-string/solutions/113435/4-lines-python/
    # the difference between a[-1:]!=a[-2:-1]and a[-1]!=a[-2]， slice won't throw error when the list only contains 1 element
    def reorganizeString(self, s: str) -> str:
        a = sorted(sorted(s), key=s.count)
        h = len(s) // 2
        a[1::2], a[::2] = a[:h], a[h:]
        return ''.join(a) * (a[-1:] != a[-2:-1])

    def reorganizeString1(self, s: str) -> str:
        c = Counter(s)
        pq = [(-v, k) for k, v in c.items()]
        heapify(pq)
        res, v2, k2 = [], 0, 0

        while pq:
            v1, k1 = heappop(pq)
            res.append(k1)
            v1 += 1
            if v2 < 0:
                heappush(pq, (v2, k2))

            v2, k2 = v1, k1

        if len(s) != len(res):
            return ''
        return ''.join(res)


def test_reorganize_string():
    solution = Solution()
    # assert solution.reorganizeString("bfrbs") == "bfbrs", 'wrong result'
    # assert solution.reorganizeString("aab") == "aba", 'wrong result'
    assert solution.reorganizeString("aaab") == "", 'wrong result'


if __name__ == '__main__':
    test_reorganize_string()
