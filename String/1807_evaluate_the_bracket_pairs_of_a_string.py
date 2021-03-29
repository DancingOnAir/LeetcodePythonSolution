from typing import List


class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        n = len(s)
        if n < 2:
            return s

        res = ''
        d = dict()
        for k in knowledge:
            d[k[0]] = k[1]

        pos = 0
        while pos < n:
            if s[pos] == '(':
                pre = pos
                while s[pos] != ')':
                    pos += 1

                key = s[pre + 1: pos]
                if key not in d:
                    res += '?'
                else:
                    res += d[key]
            else:
                res += s[pos]
            pos += 1
        return res


def test_evaluate():
    solution = Solution()
    s1 = "(name)is(age)yearsold"
    knowledge1 = [["name", "bob"], ["age", "two"]]
    assert solution.evaluate(s1, knowledge1) == "bobistwoyearsold", 'wrong result'

    s2 = "hi(name)"
    knowledge2 = [["a", "b"]]
    assert solution.evaluate(s2, knowledge2) == "hi?", 'wrong result'

    s3 = "(a)(a)(a)aaa"
    knowledge3 = [["a", "yes"]]
    assert solution.evaluate(s3, knowledge3) == "yesyesyesaaa", 'wrong result'

    s4 = "(a)(b)"
    knowledge4 = [["a", "b"], ["b", "a"]]
    assert solution.evaluate(s4, knowledge4) == "ba", 'wrong result'


if __name__ == '__main__':
    test_evaluate()
