from typing import List


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if 0 <= start < len(arr) and arr[start] >= 0:
            arr[start] = - arr[start]
            return arr[start] == 0 or self.canReach(arr, start + arr[start]) or self.canReach(arr, start - arr[start])
        return False

    def canReach1(self, arr: List[int], start: int) -> bool:
        n = len(arr)

        def dfs(i, seen):
            if i < 0 or i >= n or i in seen:
                return False
            if arr[i] == 0:
                return True
            seen.add(i)
            return dfs(i - arr[i], seen) or dfs(i + arr[i], seen)

        seen = set()
        return dfs(start, seen)


def test_can_reach():
    solution = Solution()
    assert solution.canReach([4, 2, 3, 0, 3, 1, 2], 5), 'wrong result'
    assert solution.canReach([4, 2, 3, 0, 3, 1, 2], 0), 'wrong result'
    assert not solution.canReach([3, 0, 2, 1, 2], 2), 'wrong result'


if __name__ == '__main__':
    test_can_reach()
