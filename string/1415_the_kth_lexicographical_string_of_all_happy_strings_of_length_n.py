from collections import deque


class Solution:
    # bfs
    def getHappyString(self, n: int, k: int) -> str:
        next_letter = {'a': 'bc', 'b': 'ac', 'c': 'ab'}
        q = deque(['a', 'b', 'c'])
        print(q[0])
        while len(q[0]) != n:
            u = q.popleft()
            for v in next_letter[u[-1]]:
                q.append(u + v)
        return q[k - 1] if len(q) >= k else ''

    # dfs
    def getHappyString2(self, n: int, k: int) -> str:
        def dfs(path=''):
            if len(res) == k:
                return

            if len(path) == n:
                res.append(path)
                return

            for x in 'abc':
                if not path or x != path[-1]:
                    dfs(path + x)

        res = list()
        dfs()
        return res[-1] if len(res) == k else ''

    # math
    def getHappyString1(self, n: int, k: int) -> str:
        prem = 1 << (n - 1)
        if k > 3 * prem:
            return ""

        res = ['a', 'b', 'c'][(k - 1) // prem]
        while prem > 1:
            k = (k - 1) % prem + 1
            prem >>= 1
            res += ['a', 'b'][res[-1] == 'a'] if (k - 1) // prem == 0 else ['b', 'c'][res[-1] != 'c']
        return res


def test_et_happy_string():
    solution = Solution()

    assert solution.getHappyString(1, 3) == "c", 'wrong result'
    assert solution.getHappyString(1, 4) == "", 'wrong result'
    assert solution.getHappyString(3, 9) == "cab", 'wrong result'
    assert solution.getHappyString(2, 7) == "", 'wrong result'
    assert solution.getHappyString(10, 100) == "abacbabacb", 'wrong result'


if __name__ == '__main__':
    test_et_happy_string()
