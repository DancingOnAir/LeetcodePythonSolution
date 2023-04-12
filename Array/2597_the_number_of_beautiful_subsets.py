from typing import List


class Solution:
    # backtracking
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        # 减去空集
        res = -1
        cnt = [0] * (max(nums) + 2 * k)

        def dfs(i):
            nonlocal res
            res += 1

            if i == len(nums):
                return
            for j in range(i, len(nums)):
                x = nums[j]
                if cnt[x - k] == 0 and cnt[x + k] == 0:
                    cnt[x] += 1
                    dfs(j + 1)
                    cnt[x] -= 1

        dfs(0)
        return res


def test_beautiful_subsets():
    solution = Solution()
    assert solution.beautifulSubsets([2, 4, 6], 2) == 4, 'wrong result'
    assert solution.beautifulSubsets([1], 1) == 1, 'wrong result'


if __name__ == '__main__':
    test_beautiful_subsets()
