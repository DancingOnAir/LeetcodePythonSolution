class Solution:
    def transformStr(self, s: str, strs: list[str]) -> list[bool]:
        s_zeros = s.count("0")

        def helper(t: str) -> bool:
            t_zeros = t.count("0")
            t_questions = t.count("?")
            if s_zeros < t_zeros or s_zeros > t_zeros + t_questions:
                return False

            t = list(t)
            for i, c in enumerate(t):
                if t_zeros == s_zeros:
                    break
                if c == "?":
                    t[i] = '0'
                    t_zeros += 1

            i = j = 0
            for _ in range(s_zeros):
                while s[i] != "0":
                    i += 1
                while t[j] != "0":
                    j += 1
                if i < j:
                    return False
                i += 1
                j += 1
            return True

        return list(map(helper, strs))


def test_transform_str():
    solution = Solution()
    assert solution.transformStr("101", strs = ["1?1","0?1","0?0"]) == [True,True,False], 'wrong result'
    assert solution.transformStr("1100", strs = ["0011","11?1","1?1?"]) == [True,False,True], 'wrong result'
    assert solution.transformStr("1010", strs = ["0011"]) == [True], 'wrong result'


if __name__ == '__main__':
    test_transform_str()

