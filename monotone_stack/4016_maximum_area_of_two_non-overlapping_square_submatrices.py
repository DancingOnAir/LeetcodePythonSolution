class Solution:
    def calc(self, mat: list[list[int]]) -> int:
        m, n = len(mat), len(mat[0])
        # 按0221方法计算
        # 计算mat下半部分的正大正方形边长
        suf_max = [0] * (m + 1)
        dp = [0] * (n + 1)
        for i in range(m - 1, 0, -1):
            last = 0
            for j, x in enumerate(mat[i]):
                if x:
                    tmp = dp[j + 1]
                    dp[j + 1] = min(last, dp[j + 1], dp[j]) + 1
                    last = tmp
                else:
                    dp[j + 1] = 0
                    last = 0
            suf_max[i] = max(suf_max[i + 1], max(dp))

        res = pre_max = 0
        dp = [0] * (n + 1)
        for i, row in enumerate(mat):
            last = 0
            for j, x in enumerate(row):
                if x:
                    tmp = dp[j + 1]
                    dp[j + 1] = min(last, dp[j + 1], dp[j]) + 1
                    last = tmp
                else:
                    dp[j + 1] = 0
                    last = 0
            if suf_max[i + 1] <= res:
                break
            pre_max = max(pre_max, max(dp))
            res = max(res, min(pre_max, suf_max[i + 1]))
        return res * res

    def maxArea(self, mat: list[list[int]]) -> int:
        return max(self.calc(mat), self.calc(list(zip(*mat))))


def test_max_area():
    solution = Solution()
    assert solution.maxArea([[1, 1, 1, 0], [1, 1, 1, 1], [0, 0, 1, 1]]) == 4, 'wrong result'
    assert solution.maxArea([[0, 1], [1, 0]]) == 1, 'wrong result'
    assert solution.maxArea([[0, 0], [0, 1]]) == 0, 'wrong result'


if __name__ == '__main__':
    test_max_area()
