from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(target, path, idx):
            if not target:
                res.append(path[:])
                return

            for i, val in enumerate(candidates[idx:]):
                if target >= val:
                    dfs(target - val, path + [val], idx + i)
                else:
                    break

        dfs(target, [], 0)
        return res

    def backtrack(self, candidates: List[int], target: int, res: List[List[int]], temp: List[int], depth: int, sum: int) -> None:
        if depth >= len(candidates):
            return

        if sum == target:
            res.append(temp[:])
            return

        if sum > target:
            return

        temp.append(candidates[depth])
        self.backtrack(candidates, target, res, temp, depth, sum + candidates[depth])
        temp.pop()
        self.backtrack(candidates, target, res, temp, depth + 1, sum)

    # backtrack method
    def combinationSum1(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        if not candidates:
            return res

        temp = []
        candidates.sort()
        self.backtrack(candidates, target, res, temp, 0, 0)

        return res


def test_combination_sum():
    solution = Solution()

    # candidates1 = [2, 3, 6, 7]
    # target1 = 7
    # print(solution.combinationSum(candidates1, target1))

    candidates2 = [2, 3, 5]
    target2 = 8
    print(solution.combinationSum(candidates2, target2))


if __name__ == '__main__':
    test_combination_sum()
