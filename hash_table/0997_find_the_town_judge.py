class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        cnt = [0] * (n + 1)
        for x, y in trust:
            cnt[x] -= 1
            cnt[y] += 1

        for i in range(1, n + 1):
            if cnt[i] == n - 1:
                return i
        return -1


def test_find_judge():
    solution = Solution()
    assert solution.findJudge(2, trust=[[1, 2]]) == 2, 'wrong result'
    assert solution.findJudge(3, trust=[[1, 3], [2, 3]]) == 3, 'wrong result'
    assert solution.findJudge(3, trust=[[1, 3], [2, 3], [3, 1]]) == -1, 'wrong result'


if __name__ == '__main__':
    test_find_judge()
