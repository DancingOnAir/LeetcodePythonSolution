class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
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
