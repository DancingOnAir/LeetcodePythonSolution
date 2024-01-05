from collections import Counter
from heapq import heappop, heappush, heapify


class Solution:
    def reorganizeString(self, s: str) -> str:
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
