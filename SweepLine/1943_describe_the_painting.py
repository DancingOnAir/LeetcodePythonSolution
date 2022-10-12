from typing import List
from collections import defaultdict


class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        d = defaultdict(int)
        for i, j, k in segments:
            d[i] += k
            d[j] -= k

        res = list()
        color, prev = 0, None
        for now in sorted(d):
            # if color == 0, it means this part isn't painted.
            if color:
                res.append([prev, now, color])
            color += d[now]
            prev = now

        return res

    def splitPainting1(self, segments: List[List[int]]) -> List[List[int]]:
        endpoints = list()
        for i, j, k in segments:
            endpoints.append([i, k])
            endpoints.append([j, -k])

        res = list()
        cur = pre = 0
        for i, val in sorted(endpoints):
            if pre == 0:
                pre = i
            else:
                # 如果i == pre说明2个在同一起点或终点，不需要操作，计算累加值即可
                if i > pre:
                    # 如果累加值为0，那么说明没有颜色，不需要记录
                    if cur > 0:
                        res.append([pre, i, cur])
                    pre = i
            cur += val

        return res


def test_split_painting():
    solution = Solution()
    assert solution.splitPainting([[4,16,12],[9,10,15],[18,19,13],[3,13,20],[12,16,3],[2,10,10],[3,11,4],[13,16,6]]) == [[2,3,10],[3,4,34],[4,9,46],[9,10,61],[10,11,36],[11,12,32],[12,13,35],[13,16,21],[18,19,13]], 'wrong result'
    assert solution.splitPainting([[1, 4, 5], [4, 7, 7], [1, 7, 9]]) == [[1, 4, 14], [4, 7, 16]], 'wrong result'
    assert solution.splitPainting([[1, 7, 9], [6, 8, 15], [8, 10, 7]]) == [[1, 6, 9], [6, 7, 24], [7, 8, 15], [8, 10, 7]], 'wrong result'
    assert solution.splitPainting([[1, 4, 5], [1, 4, 7], [4, 7, 1], [4, 7, 11]]) == [[1, 4, 12], [4, 7, 12]], 'wrong result'


if __name__ == '__main__':
    test_split_painting()
