from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = set()
        for bitmask in range(1 << n):
            cur = [nums[i] for i in range(n) if (bitmask >> i) & 1]
            if len(cur) > 1 and all(cur[i] <= cur[i + 1] for i in range(len(cur) - 1)):
                res.add(tuple(cur))
        return res

    # original brute force
    def findSubsequences1(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n < 2:
            return [[]]

        res = list()
        for i in range(1 << n):
            bits = bin(i).count('1')
            if bits >= 2:
                stk = list()
                flag = True
                for j in range(n):
                    if i & (1 << (n - j - 1)) > 0:
                        if stk and stk[-1] > nums[j]:
                            flag = False
                            break
                        stk.append(nums[j])

                if flag and stk not in res:
                    res.append(stk)
        return res


def test_find_subsequences():
    solution = Solution()
    res1 = solution.findSubsequences([4, 6, 7, 7])
    assert len(res1) == 8, 'wrong result'
    for x in res1:
        assert x in [[4, 6], [4, 6, 7], [4, 6, 7, 7], [4, 7], [4, 7, 7], [6, 7], [6, 7, 7], [7, 7]], 'wrong result'

    res2 = solution.findSubsequences([4, 4, 3, 2, 1])
    assert len(res2) == 1, 'wrong result'
    for x in res2:
        assert x in [[4, 4]], 'wrong result'


if __name__ == '__main__':
    test_find_subsequences()
