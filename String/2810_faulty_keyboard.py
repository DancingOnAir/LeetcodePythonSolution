class Solution:
    def finalString(self, s: str) -> str:
        res = []
        for i, c in enumerate(s):
            if c == 'i':
                res.reverse()
            else:
                res.append(c)
        return ''.join(res)


def test_final_string():
    solution = Solution()
    assert solution.finalString("string") == "rtsng", 'wrong result'
    assert solution.finalString("poiinter") == "ponter", 'wrong result'


if __name__ == '__main__':
    test_final_string()
