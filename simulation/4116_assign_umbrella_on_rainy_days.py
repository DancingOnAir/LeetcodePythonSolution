class Solution:
    def assignUmbrella(self, rain: list[int]) -> list[str]:
        res = []
        cnt1 = cnt2 = 0
        for i, x in enumerate(rain):
            if x == 0:
                res.append('None')
            elif x == 1:
                if i < len(rain) - 1 and rain[i + 1] == 1 and cnt1 <= cnt2:
                    res.append('Alice')
                    cnt1 += 1
                else:
                    res.append('Bob')
                    cnt2 += 1
        return res


def test_assign_umbrella():
    solution = Solution()
    assert solution.assignUmbrella([1, 1, 0, 1, 1]) == ["Alice", "Bob", "None", "Alice", "Bob"], 'wrong result'
    assert solution.assignUmbrella([0, 1, 0, 1]) == ["None", "Bob", "None", "Bob"], 'wrong result'


if __name__ == '__main__':
    test_assign_umbrella()
