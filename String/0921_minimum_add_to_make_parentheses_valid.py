class Solution:
    def minAddToMakeValid(self, s: str) -> int:
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
