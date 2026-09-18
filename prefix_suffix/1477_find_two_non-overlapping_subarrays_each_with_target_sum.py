class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        l = tot = 0
        pre_min = [float('inf')] * n
        res = min_len = float('inf')
        for r in range(n):
            tot += arr[r]
            while tot > target:
                tot -= arr[l]
                l += 1

            if tot == target:
                cur_len = r - l + 1

                if l > 0 and pre_min[l - 1] != float('inf'):
                    res = min(res, cur_len + pre_min[l - 1])

                min_len = min(min_len, cur_len)
            pre_min[r] = min_len

        return -1 if res == float('inf') else res

    def minSumOfLengths1(self, arr: list[int], target: int) -> int:
        n = len(arr)
        suf = [0] * n
        min_len = float('inf')
        r = n - 1
        tot = 0
        for l in range(n - 1, 0, -1):
            tot += arr[l]
            while tot > target:
                tot -= arr[r]
                r -= 1
            if tot == target:
                min_len = min(min_len, r - l + 1)
            suf[l] = min_len

        res = float('inf')
        l = tot = 0
        for r in range(n - 1):
            tot += arr[r]
            while tot > target:
                tot -= arr[l]
                l += 1
            if tot == target:
                res = min(res, r - l + 1 + suf[r + 1])
        return -1 if res == float('inf') else res


def test_min_sum_of_lengths():
    solution = Solution()
    assert solution.minSumOfLengths([3, 2, 2, 4, 3], target=3) == 2, 'wrong result'
    assert solution.minSumOfLengths([7, 3, 4, 7], target=7) == 2, 'wrong result'
    assert solution.minSumOfLengths([4, 3, 2, 6, 2, 3, 4], target=6) == -1, 'wrong result'


if __name__ == '__main__':
    test_min_sum_of_lengths()
