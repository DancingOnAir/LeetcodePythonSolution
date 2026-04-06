class Solution:
    def threeSumMulti(self, arr: list[int], target: int) -> int:
        mx = max(arr)
        m = [0] * (mx + 1)
        for x in arr:
            m[x] += 1

        MOD = 1_000_000_007
        res = 0
        for i in range(mx + 1):
            if m[i] == 0:
                continue
            left, right = i, mx
            if i + 2 * left > target:
                break
            if i + 2 * right < target:
                continue
            while left <= right:
                if i + left + right > target:
                    right -= 1
                elif i + left + right < target:
                    left += 1
                else:
                    if i == left == right:
                        res += m[i] * (m[i] - 1) * (m[i] - 2) // 6 % MOD
                    elif i == left:
                        res += m[i] * (m[i] - 1) // 2 * m[right] % MOD
                    elif left == right:
                        res += m[left] * (m[left] - 1) // 2 * m[i] % MOD
                    else:
                        res += m[i] * m[left] * m[right] % MOD
                    left += 1
                    right -= 1
        return res


def test_three_sum_multi():
    solution = Solution()
    assert solution.threeSumMulti([1, 1, 2, 2, 3, 3, 4, 4, 5, 5], target=8) == 20, 'wrong result'
    assert solution.threeSumMulti([1, 1, 2, 2, 2, 2], target=5) == 12, 'wrong result'
    assert solution.threeSumMulti([2, 1, 3], target=6) == 1, 'wrong result'


if __name__ == '__main__':
    test_three_sum_multi()
