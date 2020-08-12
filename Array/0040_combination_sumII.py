from typing import List
from functools import reduce


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def helper(candidates, target, idx, path):
            if not target:
                res.append(path[:])
                return

            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue

                if candidates[i] > target:
                    break

                helper(candidates, target - candidates[i], i + 1, path + [candidates[i]])

        helper(candidates, target, 0, [])
        return res

    def combination_sum_2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(candidates, target, path):
            if not target:
                res.append(path[:])
                return

            for i, val in enumerate(candidates):
                if target >= val:
                    dfs(candidates[i + 1:], target - val, path + [val])
                else:
                    break

        dfs(candidates, target, [])

        res = reduce((lambda x, y: x if y in x else x + [y]), [[]] + res)
        return res


def test_combination_sum2():
    solution = Solution()

    candidates1 = [10, 1, 2, 7, 6, 1, 5]
    target1 = 8
    print(solution.combinationSum2(candidates1, target1))

    candidates2 = [2, 5, 2, 1, 2]
    target2 = 5
    print(solution.combinationSum2(candidates2, target2))


if __name__ == '__main__':
    test_combination_sum2()
