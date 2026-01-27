from typing import List


class Solution:
    def maxPoints(self, technique1: List[int], technique2: List[int], k: int) -> int:
        res = 0
        cnt = 0
        diffs = []
        for a, b in zip(technique1, technique2):
            if a >= b:
                res += a
                cnt += 1
            else:
                res += b
                diffs.append(b - a)

        if cnt < k:
            diffs.sort()
            res -= sum(diffs[:k - cnt])
        return res

    def maxPoints1(self, technique1: List[int], technique2: List[int], k: int) -> int:
        n = len(technique1)
        diffs = []
        for i in range(n):
            diffs.append((technique1[i] - technique2[i], technique2[i]))
        diffs.sort()

        res = 0
        while k > 0:
            res += sum(diffs.pop())
            k -= 1

        while diffs:
            cur = diffs.pop()
            if cur[0] < 0:
                res += cur[1]
            else:
                res += cur[0] + cur[1]
        return res


def test_max_points():
    solution = Solution()
    assert solution.maxPoints([5, 2, 10], [10, 3, 8], 2) == 22, 'wrong result'
    assert solution.maxPoints([10, 20, 30], [5, 15, 25], 2) == 60, 'wrong result'
    assert solution.maxPoints([1, 2, 3], [4, 5, 6], 0) == 15, 'wrong result'


if __name__ == '__main__':
    test_max_points()
