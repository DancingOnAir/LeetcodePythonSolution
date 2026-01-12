from typing import List
from collections import defaultdict, Counter


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        return max([k for k, v in Counter(arr).items() if k == v] + [-1])

    def findLucky1(self, arr: List[int]) -> int:
        counts = defaultdict(int)
        res = -1
        for a in arr:
            counts[a] += 1

        for k, v in counts.items():
            if k == v:
                res = max(res, k)
        return res


def test_find_lucky():
    solution = Solution()

    arr1 = [2, 2, 3, 4]
    print(solution.findLucky(arr1))

    arr2 = [1, 2, 2, 3, 3, 3]
    print(solution.findLucky(arr2))

    arr3 = [2, 2, 2, 3, 3]
    print(solution.findLucky(arr3))

    arr4 = [5]
    print(solution.findLucky(arr4))

    arr5 = [7, 7, 7, 7, 7, 7, 7]
    print(solution.findLucky(arr5))


if __name__ == '__main__':
    test_find_lucky()
