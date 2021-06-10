from typing import List
from itertools import product


class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        stk = [set(), {''}]
        for c in expression:
            if c == '{':
                # 压入当前层已知元素
                stk.append(set())
                # 压入当前层未知元素
                stk.append({''})
            elif c == '}':
                # 未知元素出栈
                unknow = stk.pop()
                # 合并两个集合，由于遇见}，未确定集合可以并入已知集合
                know = stk.pop() | unknow
                # 将当前层遇上一层未确定元素做笛卡尔积，完成出栈。
                stk[-1] = {i + j for i in stk[-1] for j in know}
            elif c == ',':
                # 将未确定元素加入确定集合中
                stk[-2] = stk[-1] | stk[-2]
                # 未确定元素清零
                stk[-1] = {''}
            else:
                # 输入为字母，直接与未确定元素集合做笛卡尔积
                stk[-1] = {i + c for i in stk[-1]}

        return sorted(list(stk[-1] | stk[-2]))

    def braceExpansionII2(self, expression: str) -> List[str]:
        pre = list()
        cur = list()
        stk = list()

        for i, c in enumerate(expression):
            if c == '{':
                stk.append(pre)
                stk.append(cur)
                pre = list()
                cur = list()
            elif c == '}':
                last = stk.pop()
                second_last = stk.pop()

                cur = [j + i for i in pre + cur for j in last or ['']]
                pre = second_last
            elif c == ',':
                pre += cur
                cur = list()
            elif c.isalpha():
                cur = [x + c for x in cur or ['']]

        return sorted(set(pre + cur))

    # https://leetcode.com/problems/brace-expansion-ii/discuss/317623/Python3-Clear-and-Short-Recursive-Solution
    def braceExpansionII1(self, expression: str) -> List[str]:
        groups = [[]]
        level = 0

        for i, c in enumerate(expression):
            if c == '{':
                if level == 0:
                    start = i + 1
                level += 1

            elif c == '}':
                level -= 1
                if level == 0:
                    groups[-1].append(self.braceExpansionII(expression[start: i]))

            elif c == ',' and level == 0:
                groups.append([])
            elif level == 0:
                groups[-1].append([c])

        res = set()
        # pythonic method 1
        # for group in groups:
        #     res |= set(map(''.join, product(*group)))

        # regular method 2
        for g in groups:
            while len(g) > 1:
                # take care the s1 & s2 sequence
                s2 = g.pop()
                s1 = g.pop()
                temp = [i + j for i in s1 for j in s2]
                g.append(temp)
            res.update(g.pop())

        return sorted(res)


def test_brace_expansion():
    solution = Solution()
    # print(solution.braceExpansionII('{a{b,c},d{e,f}{g,{j,k}{h,i{x,y{z,w}}}}}'))
    # assert solution.braceExpansionII('{a{b,c}}') == ["ab", "ac"], 'wrong result'
    assert solution.braceExpansionII('{a,b}{c,{d,e}}') == ["ac", "ad", "ae", "bc", "bd", "be"], 'wrong result'
    assert solution.braceExpansionII('{{a,z},a{b,c},{ab,z}}') == ["a", "ab", "ac", "z"], 'wrong result'


if __name__ == '__main__':
    test_brace_expansion()
