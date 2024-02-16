from typing import List


class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        n = len(num)
        res = []

        def dfs(i, arr):
            if len(arr) >= 3 and i == n:
                nonlocal res
                res = arr.copy()
                return
            if i == n:
                return
            for j in range(i, n):
                if num[i] == '0' and j > i:
                    return
                if int(num[i: j+1]) > 2 ** 31 - 1 or int(num[i: j+1]) < 0:
                    continue
                if len(arr) < 2:
                    dfs(j + 1, arr + [int(num[i: j+1])])
                else:
                    if int(num[i: j+1]) == arr[-2] + arr[-1]:
                        dfs(j + 1, arr + [int(num[i: j+1])])

        dfs(0, [])
        return res


def test_split_into_fibonacci():
    solution = Solution()
    # assert solution.splitIntoFibonacci("1101111") == [11, 0, 11, 11], 'wrong result'
    assert solution.splitIntoFibonacci("112358130") == [], 'wrong result'
    assert solution.splitIntoFibonacci("0123") == [], 'wrong result'


if __name__ == '__main__':
    test_split_into_fibonacci()
