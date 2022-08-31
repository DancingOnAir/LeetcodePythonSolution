from typing import List


class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        def find(x):
            if x != parents[x]:
                parents[x] = find(parents[x])
            return parents[x]

        n = len(nums)
        parents = list(range(n + 1))
        total = [0] * (n + 1)
        res = [0] * n
        for i in range(n - 1, 0, -1):
            x = removeQueries[i]
            pa = find(x + 1)
            # 将x和x+1合并
            parents[x] = pa

            total[pa] += total[x] + nums[x]
            res[i - 1] = max(res[i], total[pa])
        return res


def test_maximum_segment_sum():
    solution = Solution()
    assert solution.maximumSegmentSum([1, 2, 5, 6, 1], [0, 3, 2, 4, 1]) == [14, 7, 2, 2, 0], 'wrong result'
    assert solution.maximumSegmentSum([3, 2, 11, 1], [3, 2, 1, 0]) == [16, 5, 3, 0], 'wrong result'


if __name__ == '__main__':
    test_maximum_segment_sum()

