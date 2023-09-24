from typing import List


class Solution:
    # backtracking mode1
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = -1
        cnt = [0] * (max(nums) + k + 1)

        def dfs(i):
            if i == n:
                nonlocal res
                res += 1
                return

            dfs(i + 1)
            if cnt[nums[i] - k] == 0 and cnt[nums[i] + k] == 0:
                cnt[nums[i]] += 1
                dfs(i + 1)
                cnt[nums[i]] -= 1

        dfs(0)
        return res

    # backtracking mode2
    def beautifulSubsets1(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # - 1 for the empty set
        res = -1
        cnt = [0] * (max(nums) + k + 1)

        def dfs(i):
            nonlocal res
            res += 1

            if i == n:
                return
            for j in range(i, n):
                if cnt[nums[j] - k] == 0 and cnt[nums[j] + k] == 0:
                    cnt[nums[j]] += 1
                    dfs(j + 1)
                    cnt[nums[j]] -= 1

        dfs(0)
        return res


def test_beautiful_subsets():
    solution = Solution()
    assert solution.beautifulSubsets([2, 4, 6], 2) == 4, 'wrong result'
    assert solution.beautifulSubsets([1], 1) == 1, 'wrong result'


if __name__ == '__main__':
    test_beautiful_subsets()
