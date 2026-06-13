from typing import List


class Solution:
    # trie
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        trie = {}
        n = len(nums)
        res = 0
        for i in range(n):
            cnt = 0
            root = trie
            for j in range(i, n):
                x = nums[j]
                if x % p == 0:
                    cnt += 1
                if cnt > k:
                    break

                if x not in root:
                    root[x] = {}
                    res += 1
                root = root[x]
        return res

    # sliding window
    def countDistinct1(self, nums: List[int], k: int, p: int) -> int:
        cnt = 0
        left = 0
        res = set()
        for right in range(len(nums)):
            if nums[right] % p == 0:
                cnt += 1

            while left <= right and cnt > k:
                if nums[left] % p == 0:
                    cnt -= 1
                left += 1

            for i in range(left, right + 1):
                res.add(tuple(nums[i: right+1]))

        return len(res)


def test_count_distinct():
    solution = Solution()
    assert solution.countDistinct([2, 3, 3, 2, 2], 2, 2) == 11, 'wrong result'
    assert solution.countDistinct([1, 2, 3, 4], 4, 1) == 10, 'wrong result'


if __name__ == '__main__':
    test_count_distinct()
