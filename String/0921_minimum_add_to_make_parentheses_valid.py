class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        while '()' in s:
            s = s.replace('()', '')
        return len(s)

    def minAddToMakeValid2(self, s: str) -> int:
        left = right = 0
        for c in s:
            if c == '(':
                right += 1
            elif right > 0:
                right -= 1
            else:
                left += 1
        return left + right

    def minAddToMakeValid1(self, s: str) -> int:
        stk = list()
        closing_bracket = 0
        for c in s:
            if c == '(':
                stk.append(c)
            else:
                if stk and stk[-1] == '(':
                    stk.pop()
                else:
                    closing_bracket += 1
        return len(stk) + closing_bracket


def test_min_add_to_make_valid():
    solution = Solution()

    assert solution.minAddToMakeValid("())") == 1, 'wrong result'
    assert solution.minAddToMakeValid("(((") == 3, 'wrong result'


if __name__ == '__main__':
    test_min_add_to_make_valid()
