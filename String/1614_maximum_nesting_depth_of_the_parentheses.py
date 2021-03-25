class Solution:
    def maxDepth(self, s: str) -> int:
        res, count = 0, 0
        for c in s:
            if c == '(':
                count += 1
            elif c == ')':
                count -= 1
            res = max(res, count)

        return res


def test_max_depth():
    solution = Solution()
    assert solution.maxDepth('(1+(2*3)+((8)/4))+1') == 3, 'wrong result'
    assert solution.maxDepth('(1)+((2))+(((3)))') == 3, 'wrong result'
    assert solution.maxDepth('1+(2*3)/(2-1)') == 1, 'wrong result'
    assert solution.maxDepth('1') == 0, 'wrong result'
    assert solution.maxDepth('((8+7)*(3+9)-0)*(1*6)') == 2, 'wrong result'


if __name__ == '__main__':
    test_max_depth()
