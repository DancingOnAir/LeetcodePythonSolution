from typing import List
from bisect import bisect_right


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (x[0], -x[1]))
        tree = [0] * 4096
        n = len(people)

        res = [[] for _ in range(n)]
        X = 2048
        i = 2
        k = X
        l = 1
        while i <= 4096:
            for j in range(i // 2, 0, -1):
                tree[l] = k
                l += 1
            k >>= 1
            i <<= 1

        for i in range(n):
            j = 1
            while j < X:
                k = people[i][1]
                j <<= 1

                if k >= tree[j]:
                    k -= tree[j]
                    j += 1

                tree[j] -= 1

            res[j - X] = people[i]
        return res

    # sort and insert
    def reconstructQueue3(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda p: (-p[0], p[1]))
        res = list()
        for p in people:
            res.insert(p[1], p)
        return res

    # sort and find the empty space for current person
    def reconstructQueue2(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda p: (p[0], -p[1]))
        res = [[] for _ in range(len(people))]
        for p in people:
            space = p[1] + 1
            for i in range(len(people)):
                if not res[i]:
                    space -= 1
                    if space == 0:
                        res[i] = p
                        break
        return res

    # TLE
    def reconstructQueue1(self, people: List[List[int]]) -> List[List[int]]:
        people = sorted(people, key=lambda x: (x[1], x[0]))

        n = len(people)
        res = list()
        while len(res) < n:
            cur = list()
            for i, p in enumerate(people):
                if p not in res and p[1] == bisect_right(res, p):
                    cur.append(p)

            res += list(sorted(cur))
        return res


def test_reconstruct_queue():
    solution = Solution()
    assert solution.reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]) == [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]], 'wrong result'
    assert solution.reconstructQueue([[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]) == [[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]], 'wrong result'


if __name__ == '__main__':
    test_reconstruct_queue()
