class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def dfs(idx, tmp):
            if len(s) == idx:
                return len(tmp) if tmp[-1] not in tmp[:-1] else 0
            if tmp[-1] in tmp[:-1]:
                return dfs(idx+1, tmp[:-1] + [tmp[-1]+s[idx]])
            return max(dfs(idx+1, tmp[:-1] + [tmp[-1]+s[idx]]), dfs(idx+1, tmp + [s[idx]]))
        return dfs(1, [s[0]])


def test_max_unique_split():
    solution = Solution()
    # assert solution.maxUniqueSplit('ababccc') == 5, 'wrong result'
    assert solution.maxUniqueSplit('aba') == 2, 'wrong result'
    assert solution.maxUniqueSplit('aa') == 1, 'wrong result'


if __name__ == '__main__':
    test_max_unique_split()
