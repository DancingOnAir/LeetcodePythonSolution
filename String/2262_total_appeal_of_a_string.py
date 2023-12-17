class Solution:
    # https://leetcode.cn/problems/total-appeal-of-a-string/solutions/1461618/by-endlesscheng-g405/
    def appealSum(self, s: str) -> int:
        res, total, last = 0, 0, {}
        for i, ch in enumerate(s):
            total += i - last.get(ch, -1)
            res += total
            last[ch] = i
        return res


def test_appeal_sum():
    solution = Solution()
    assert solution.appealSum("abbca") == 28, 'wrong result'
    assert solution.appealSum("code") == 20, 'wrong result'


if __name__ == '__main__':
    test_appeal_sum()
