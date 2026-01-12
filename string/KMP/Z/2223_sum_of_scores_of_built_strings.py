class Solution:
    def sumScores(self, s: str) -> int:
        def cal_z(w):
            n = len(w)
            z = [0] * n
            l, r = 0, 0
            for i in range(1, n):
                if i < r:
                    z[i] = max(0, min(z[i - l], r - i + 1))
                while z[i] + i < n and s[z[i]] == s[z[i] + i]:
                    l, r = i, z[i] + i
                    z[i] += 1

            z[0] = n
            return z

        return sum(cal_z(s))


def test_sum_scores():
    solution = Solution()
    assert solution.sumScores("babab") == 9, 'wrong result'
    assert solution.sumScores("azbazbzaz") == 14, 'wrong result'


if __name__ == '__main__':
    test_sum_scores()
