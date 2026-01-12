class Solution:
    def decodeString(self, s: str) -> str:
        stk = list()
        for ch in s:
            if ch == ']':
                expr = ''
                while stk[-1] != '[':
                    expr = stk.pop() + expr
                stk.pop()

                num = ''
                while stk and stk[-1].isdigit():
                    num = stk.pop() + num
                stk.append(expr * int(num))
            else:
                stk.append(ch)

        return ''.join(stk)

    def decodeString1(self, s: str) -> str:
        stk = list()

        for ch in s:
            if ch == ']':
                cur_str = list()
                while stk[-1] != '[':
                    cur_str.append(stk[-1])
                    stk.pop()
                # remove '['
                stk.pop()
                cur_num = list()
                while stk and stk[-1].isdigit():
                    cur_num.append(stk[-1])
                    stk.pop()

                stk.append(''.join(reversed(cur_str)) * int(''.join(reversed(cur_num))))
            else:
                stk.append(ch)

        return ''.join(stk)


def test_decode_string():
    solution = Solution()
    assert solution.decodeString("10[a]") == "a" * 10, 'wrong result'
    assert solution.decodeString("3[a]2[bc]") == "aaabcbc", 'wrong result'
    assert solution.decodeString("3[a2[c]]") == "accaccacc", 'wrong result'
    assert solution.decodeString("2[abc]3[cd]ef") == "abcabccdcdcdef", 'wrong result'


if __name__ == '__main__':
    test_decode_string()
