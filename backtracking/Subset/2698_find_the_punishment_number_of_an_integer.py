class Solution:
    def helper(self, pre_sum):
        for i in range(1, 1001):
            s = str(i * i)
            n = len(s)

            def dfs(pos, tot):
                if pos == n:
                    return tot == i
                x = 0
                for j in range(pos, n):
                    x = x * 10 + int(s[j])
                    if dfs(j + 1, tot + x):
                        return True
                return False

            pre_sum[i] = pre_sum[i - 1] + (i * i if dfs(0, 0) else 0)

    def punishmentNumber(self, n: int) -> int:
        pre_sum = [0] * 1001
        self.helper(pre_sum)
        return pre_sum[n]


def test_punishment_number():
    solution = Solution()
    assert solution.punishmentNumber(10) == 182, 'wrong result'
    assert solution.punishmentNumber(37) == 1478, 'wrong result'


if __name__ == '__main__':
    test_punishment_number()
