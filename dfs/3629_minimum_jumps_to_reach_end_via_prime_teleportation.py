from typing import List
from collections import defaultdict


class Solution:
    def isPrime(self, x):
        if x < 2:
            return False
        if 2 == x or 3 == x:
            return True
        if x % 2 == 0 or x % 3 == 0:
            return False
        for i in range(5, int(x ** 0.5) + 1, 6):
            if x % i == 0 or x % (i + 2) == 0:
                return False
        return True

    def minJumps(self, nums: List[int]) -> int:
        m = defaultdict(list)
        for i, x in enumerate(nums):
            if self.isPrime(x):
                m[x].append(i)
        for i, x in enumerate(nums):
            for k in m:
                if x % k == 0 and x != k:
                    m[k].append(i)
        n = len(nums)
        res = 0
        seen = [False] * n
        seen[0] = True
        q = [0]
        while True:
            tmp = q
            q = []
            for i in tmp:
                if i == n - 1:
                    return res
                idx = m[nums[i]]
                idx.append(i + 1)
                if i > 0:
                    idx.append(i - 1)
                for j in idx:
                    if not seen[j]:
                        seen[j] = True
                        q.append(j)
                idx.clear()
            res += 1


def test_min_jumps():
    solution = Solution()
    assert solution.minJumps([1, 2, 4, 6]) == 2, 'wrong result'
    assert solution.minJumps([2, 3, 4, 7, 9]) == 2, 'wrong result'
    assert solution.minJumps([4, 6, 5, 8]) == 3, 'wrong result'


if __name__ == '__main__':
    test_min_jumps()
