from typing import List


class Solution:
    # check by value
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        path = [0] * n

        def dfs(i):
            if i == n:
                res.append(path.copy())
                return

            for j in range(n):
                if nums[j] > 10:
                    continue

                path[i] = nums[j]
                nums[j] += 20
                dfs(i + 1)
                nums[j] -= 20
        dfs(0)
        return res

    # check by checking list
    def permute2(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = list()
        path = [0] * n
        on_path = [False] * n

        def dfs(i):
            if i == n:
                res.append(path.copy())
                return

            for j in range(n):
                if not on_path[j]:
                    path[i] = nums[j]
                    on_path[j] = True
                    dfs(i + 1)
                    on_path[j] = False
        dfs(0)
        return res

    # check by set
    def permute1(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        n = len(nums)

        def dfs(i, s):
            if i == n:
                res.append(path.copy())
                return

            for x in s:
                path.append(x)
                dfs(i + 1, s - {x})
                path.pop()

        dfs(0, set(nums))
        return res


def test_permute():
    solution = Solution()
    assert solution.permute([1, 2, 3]) == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2],
                                           [3, 2, 1]], 'wrong result'
    assert solution.permute([0, 1]) == [[0, 1], [1, 0]], 'wrong result'
    assert solution.permute([1]) == [[1]], 'wrong result'


if __name__ == '__main__':
    test_permute()
