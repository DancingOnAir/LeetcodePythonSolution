from typing import List
from collections import defaultdict, Counter
import heapq


class Solution:
    # hash map + tree map
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        c = Counter(arr)
        cnt, remaining = Counter(c.values()), len(c)
        for key in sorted(cnt):
            if k >= key * cnt[key]:
                k -= key * cnt[key]
                remaining -= cnt.pop(key)
            else:
                return remaining - k // key
        return remaining

    # hash map + priority queue
    def findLeastNumOfUniqueInts2(self, arr: List[int], k: int) -> int:
        hp = [(val, key) for key, val in Counter(arr).items()]
        heapq.heapify(hp)
        while k > 0:
            k -= heapq.heappop(hp)[0]

        return len(hp) + (k < 0)

    def findLeastNumOfUniqueInts1(self, arr: List[int], k: int) -> int:
        dd = defaultdict(int)
        for a in arr:
            dd[a] += 1

        l = sorted(dd.items(), key=lambda obj: obj[1])
        for i, val in enumerate(l):
            if k >= val[1]:
                k -= val[1]
            else:
                return len(l) - i

        return 0


def test_find_least_num_of_unique_ints():
    solution = Solution()

    arr1 = [5, 5, 4]
    k1 = 1
    print(solution.findLeastNumOfUniqueInts(arr1, k1))

    arr2 = [4, 3, 1, 1, 3, 3, 2]
    k2 = 3
    print(solution.findLeastNumOfUniqueInts(arr2, k2))

    arr3 = [1]
    k3 = 1
    print(solution.findLeastNumOfUniqueInts(arr3, k3))


if __name__ == '__main__':
    test_find_least_num_of_unique_ints()
