class Solution:
    def sumAndMultiply(self, s: str, queries: list[list[int]]) -> list[int]:
        MOD = 10 ** 9 + 7
        n = len(s)
        pre_mul = [1] + [0] * n
        pre_sum = [0] * (n + 1)
        pre_non_zero_cnt = [0] * (n + 1)
        pre_non_zero_num = [0] * (n + 1)
        for i, c in enumerate(s):
            pre_mul[i + 1] = (pre_mul[i] * 10) % MOD
            x = int(c)
            pre_sum[i + 1] = pre_sum[i] + x
            if x != 0:
                pre_non_zero_num[i + 1] = (pre_non_zero_num[i] * 10 + x) % MOD
                pre_non_zero_cnt[i + 1] = pre_non_zero_cnt[i] + 1
            else:
                pre_non_zero_num[i + 1] = pre_non_zero_num[i]
                pre_non_zero_cnt[i + 1] = pre_non_zero_cnt[i]


        res = []
        for l, r in queries:
            num = (pre_non_zero_num[r + 1] + MOD - (pre_non_zero_num[l] * pre_mul[(pre_non_zero_cnt[r + 1] - pre_non_zero_cnt[l])] % MOD)) % MOD
            x = (pre_sum[r + 1] - pre_sum[l] + MOD) % MOD
            res.append((x * num) % MOD)
        return res


def test_sum_and_multiply():
    solution = Solution()
    assert solution.sumAndMultiply("10203004", queries = [[0,7],[1,3],[4,6]]) == [12340, 4, 9], 'wrong result'
    assert solution.sumAndMultiply("1000", queries = [[0,3],[1,1]]) == [1,0], 'wrong result'
    assert solution.sumAndMultiply("9876543210", queries = [[0,9]]) == [444444137], 'wrong result'


if __name__ == '__main__':
    test_sum_and_multiply()

