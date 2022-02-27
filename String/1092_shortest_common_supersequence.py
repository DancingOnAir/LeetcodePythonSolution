class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        l1, l2 = len(str1), len(str2)

        dp1 = [[0] * (l2+1) for _ in range(l1+1)]
        dp2 = [[0] * (l2+1) for _ in range(l1+1)]

        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp1[i][j] = dp1[i - 1][j - 1] + 1
                    dp2[i][j] = 1
                else:
                    if dp1[i - 1][j] >= dp1[i][j - 1]:
                        dp1[i][j] = dp1[i - 1][j]
                        dp2[i][j] = 2
                    else:
                        dp1[i][j] = dp1[i][j - 1]
                        dp2[i][j] = 3

        def get_one_lcs(i, j):
            if not i or not j:
                return ''
            if dp2[i][j] == 1:
                return get_one_lcs(i - 1, j - 1) + str1[i - 1]
            elif dp2[i][j] == 2:
                return get_one_lcs(i - 1, j)
            else:
                return get_one_lcs(i, j - 1)

        lcs = get_one_lcs(l1, l2)
        res = ''
        i = j = k = 0
        while i < l1 or j < l2:
            if k < len(lcs):
                p1 = str1.find(lcs[k], i)
                p2 = str2.find(lcs[k], j)

                if p1 != -1:
                    res += str1[i: p1]
                    i = p1 + 1
                if p2 != -1:
                    res += str2[j: p2]
                    j = p2 + 1
                res += lcs[k]
                k += 1
            else:
                res += str1[i:] + str2[j:]
                break

        return res


def test_shortest_common_supersequence():
    solution = Solution()

    assert solution.shortestCommonSupersequence("bbbaaaba", "bbababbb") == "bbabaaababb", 'wrong result'
    assert solution.shortestCommonSupersequence('abac', 'cab') == 'cabac', 'wrong result'
    assert solution.shortestCommonSupersequence('aaaaaaaa', 'aaaaaaaa') == 'aaaaaaaa', 'wrong result'


if __name__ == '__main__':
    test_shortest_common_supersequence()
