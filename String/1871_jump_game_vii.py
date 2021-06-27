class Solution:
    # presum + dp
    # dp[i] = 1 means it can jump from 0 to i otherwise, 0 means can not
    # pre represents sum(dp[i) i from 0 to i
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        dp = [1] + [0] * (n - 1)
        pre = [0] * n
        for i in range(1, minJump):
            pre[i] = 1
        for i in range(minJump, n):
            left, right = i - maxJump, i - minJump
            if s[i] == '0':
                total = pre[right] - (0 if left < 1 else pre[left - 1])
                dp[i] = int(total != 0)
            pre[i] = pre[i - 1] + dp[i]
        return bool(dp[-1])

    # recursive but TLE
    def canReach1(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] != '0':
            return False

        def helper(idx):
            if idx + minJump <= len(s) - 1 <= idx + maxJump:
                return True

            left = idx + minJump
            right = idx + maxJump
            pos = s.find('0', left, right + 1)
            res = False
            while pos != -1:
                res = res or helper(pos)
                pos = s.find('0', pos + 1, right + 1)
            return res

        return helper(0)


def test_can_reach():
    solution = Solution()

    assert solution.canReach('011010', 2, 3), 'wrong result'
    assert not solution.canReach('01101110', 2, 3), 'wrong result'


if __name__ == '__main__':
    test_can_reach()
