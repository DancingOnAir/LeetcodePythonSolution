class Solution:
    # stack
    def removeDuplicates(self, s: str) -> str:
        stk = list()
        for c in s:
            if stk and stk[-1] == c:
                stk.pop()
            else:
                stk.append(c)
        return ''.join(stk)

    # two pointers
    def removeDuplicates1(self, s: str) -> str:
        s = list(s)
        i = 0
        for j, c in enumerate(s):
            s[i] = s[j]
            if i > 0 and s[i] == s[i - 1]:
                i -= 2
            i += 1
        return ''.join(s[:i])


def test_remove_duplicates():
    solution = Solution()

    assert solution.removeDuplicates('abbaca') == 'ca', 'wrong result'
    assert solution.removeDuplicates('azxxzy') == 'ay', 'wrong result'


if __name__ == '__main__':
    test_remove_duplicates()
