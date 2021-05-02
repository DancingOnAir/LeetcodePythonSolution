from typing import List


class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        def backtracking(cur: List[int], total: int) -> None:
            if total == target:
                nums.add(sorted(cur[:]))
                return

            for i in range(n):
                if target < total + cost[i]:
                    continue
                cur.append(cost[i])
                backtracking(cur, total + cost[i])
                cur.pop()

        d = dict()
        for i, val in enumerate(cost):
            d[val] = i + 1
        cost = [*d.keys()]
        # cost.sort()
        n = len(cost)
        # d = [(i + 1, cost[i]) for i in range(n)]
        # d.sort(key=lambda x: (x[1], -x[0]))
        print(d)
        print(cost)
        nums = set()
        backtracking([], 0)
        print(nums)
        pass


def test_largest_number():
    solution = Solution()
    assert solution.largestNumber([4, 3, 2, 5, 6, 7, 2, 5, 5], 9) == '7772', 'wrong result'
    assert solution.largestNumber([7, 6, 5, 5, 5, 6, 8, 7, 8], 12) == '85', 'wrong result'
    assert solution.largestNumber([2, 4, 6, 2, 4, 6, 4, 4, 4], 5) == '0', 'wrong result'
    assert solution.largestNumber([6, 10, 15, 40, 40, 40, 40, 40, 40], 47) == '32211', 'wrong result'


if __name__ == '__main__':
    test_largest_number()
