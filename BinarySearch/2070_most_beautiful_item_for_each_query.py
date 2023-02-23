from typing import List
from bisect import bisect_left


class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items = sorted(items + [[0, 0]])
        for i in range(len(items) - 1):
            items[i + 1][1] = max(items[i][1], items[i + 1][1])
        return [items[bisect_left(items, [q + 1]) - 1][1] for q in queries]

    def maximumBeauty1(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        mx = 0
        for i, v in enumerate(items):
            mx = max(mx, v[1])
            items[i][1] = mx

        res = list()
        for i, v in enumerate(queries):
            l, r = 0, len(items) - 1
            while l <= r:
                mid = l + (r - l) // 2
                if items[mid][0] <= v:
                    l = mid + 1
                else:
                    r = mid - 1

            res.append(items[l - 1][1] if l > 0 else 0)
        return res


def test_maximum_beauty():
    solution = Solution()
    assert solution.maximumBeauty(
        [[193, 732], [781, 962], [864, 954], [749, 627], [136, 746], [478, 548], [640, 908], [210, 799], [567, 715],
         [914, 388], [487, 853], [533, 554], [247, 919], [958, 150], [193, 523], [176, 656], [395, 469], [763, 821],
         [542, 946], [701, 676]],
        [885, 1445, 1580, 1309, 205, 1788, 1214, 1404, 572, 1170, 989, 265, 153, 151, 1479, 1180, 875, 276, 1584]) == [
               962, 962, 962, 962, 746, 962, 962, 962, 946, 962, 962, 919, 746, 746, 962, 962, 962, 919,
               962], 'wrong result'
    assert solution.maximumBeauty([[1, 2], [3, 2], [2, 4], [5, 6], [3, 5]], [1, 2, 3, 4, 5, 6]) == [2, 4, 5, 5, 6,
                                                                                                    6], 'wrong result'
    assert solution.maximumBeauty([[1, 2], [1, 2], [1, 3], [1, 4]], [1]) == [4], 'wrong result'
    assert solution.maximumBeauty([[10, 1000]], [5]) == [0], 'wrong result'


if __name__ == '__main__':
    test_maximum_beauty()
