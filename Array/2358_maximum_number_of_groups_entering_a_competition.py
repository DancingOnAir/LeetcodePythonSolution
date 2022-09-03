from typing import List


class Solution:
    # https://leetcode.com/problems/maximum-number-of-groups-entering-a-competition/discuss/2357789/JavaC%2B%2BPython-One-line-O(1)
    # 1 + 2 + ... + k <= n
    # k(k + 1) / 2 <= n
    # (k + 0.5)(k + 0.5) <= n * 2 + 0.25
    # k + 0.5 <= sqrt(n * 2 + 0.25)
    # k <= sqrt(n * 2 + 0.25) - 0.5
    def maximumGroups(self, grades: List[int]) -> int:
        return int((len(grades) * 2 + 0.25) ** 0.5 - 0.5)

    # 不需要考虑总和，只要正整数，一定能找到一个组合满足金字塔且下层和大于上层和，那么关键是下层的数量要大于上层
    # find out the maximum result k that 1 + 2 + ... + k <= n
    def maximumGroups1(self, grades: List[int]) -> int:
        n = len(grades)
        k = 0
        while n >= k + 1:
            k += 1
            n -= k
        return k


def test_maximum_groups():
    solution = Solution()
    assert solution.maximumGroups([10, 6, 12, 7, 3, 5]) == 3, 'wrong result'
    assert solution.maximumGroups([8, 8]) == 1, 'wrong result'


if __name__ == '__main__':
    test_maximum_groups()
