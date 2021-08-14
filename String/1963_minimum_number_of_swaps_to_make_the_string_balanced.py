class Solution:
    def minSwaps(self, s: str) -> int:
        stk = list()
        res = 0
        for c in s:
            if stk and stk[-1] == '[' and c == ']':
                stk.pop()
            else:
                stk.append(c)

        res = (len(stk) // 2 + 1) // 2
        return res


def test_min_swaps():
    solution = Solution()

    assert solution.minSwaps("][][") == 1, 'wrong result'
    assert solution.minSwaps("]]][[[") == 2, 'wrong result'
    assert solution.minSwaps("[]") == 0, 'wrong result'


if __name__ == '__main__':
    test_min_swaps()
