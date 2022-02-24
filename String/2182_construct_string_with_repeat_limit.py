from collections import Counter


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        c = Counter(s)
        k = sorted(c)

        res = ''
        while len(c) > 0:
            if c[k[-1]] <= repeatLimit:
                if k[-1] == 's':
                    print(k[-1])

                res += k[-1] * c[k[-1]]

                del c[k[-1]]
                k.pop()
            else:
                res += k[-1] * repeatLimit
                c[k[-1]] -= repeatLimit

                if len(k) == 1:
                    break
                res += k[-2]
                c[k[-2]] -= 1
                if c[k[-2]] == 0:
                    del c[k[-2]]
                    k.pop(-2)

        return res


def test_repeat_limited_string():
    solution = Solution()
    assert solution.repeatLimitedString('xyutfpopdynbadwtvmxiemmusevduloxwvpkjioizvanetecnuqbqqdtrwrkgt', 1) == 'zyxyxwxwvwvuvuvututstrtrtqpqpqponononmlmkmkjigifiededededcbaba', 'wrong result'
    assert solution.repeatLimitedString('cczazcc', 3) == 'zzcccac', 'wrong result'
    assert solution.repeatLimitedString('aababab', 2) == 'bbabaa', 'wrong result'


if __name__ == '__main__':
    test_repeat_limited_string()
