from typing import List
from collections import defaultdict


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        da = defaultdict(set)
        db = defaultdict(set)
        dc = defaultdict(set)

        for i in range(len(arr) - 1):
            for j in range(i + 1, len(arr)):
                dis = abs(arr[i] - arr[j])
                if dis <= a:
                    da[i].add(j)
                if dis <= b:
                    db[i].add(j)
                if dis <= c:
                    dc[i].add(j)
        res = 0
        for i in range(len(arr) - 2):
            for j in da[i]:
                for k in db[j]:
                    if k in dc[i]:
                        res += 1
        return res

    def countGoodTriplets2(self, arr: List[int], a: int, b: int, c: int) -> int:
        res, n = 0, len(arr)
        for i in range(n):
            for k in range(i + 2, n):
                if abs(arr[i] - arr[k]) > c:
                    continue
                res += sum(abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b for j in range(i + 1, k))
        return res

    def countGoodTriplets1(self, arr: List[int], a: int, b: int, c: int) -> int:
        res = 0

        n = len(arr)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        res += 1
        return res


def test_count_good_triplets():
    solution = Solution()

    arr1 = [3, 0, 1, 1, 9, 7]
    a1 = 7
    b1 = 2
    c1 = 3
    print(solution.countGoodTriplets(arr1, a1, b1, c1))

    arr2 = [1, 1, 2, 2, 3]
    a2 = 0
    b2 = 0
    c2 = 1
    print(solution.countGoodTriplets(arr2, a2, b2, c2))


if __name__ == '__main__':
    test_count_good_triplets()
