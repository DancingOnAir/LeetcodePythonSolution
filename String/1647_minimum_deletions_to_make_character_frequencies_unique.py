from collections import Counter


class Solution:
    def minDeletions1(self, s: str) -> int:
        c = Counter(Counter(s).values())
        k = set(c.keys())
        v = [(k, v-1)for k, v in c.items() if v > 1]
        v.sort(key=lambda x: x[0])

        res = 0
        if not v:
            return res

        target = max(k) - 1
        while v:
            cur = v.pop()
            target = min(target, cur[0] - 1)
            for i in range(cur[1]):
                while target in k and target > 0:
                    target -= 1
                res += cur[0] - target

                if target > 0:
                    target -= 1

        return res


def test_min_deletions():
    solution = Solution()

    # assert solution.minDeletions('bogoidmdkbllehemdkfofcieckdoffiokflejeeffhihfbbfffboklaoochielobmcekaeoajicke') == 19, 'wrong result'
    assert solution.minDeletions('accdcdadddbaadbc') == 1, 'wrong result'
    assert solution.minDeletions('aab') == 0, 'wrong result'
    assert solution.minDeletions('aaabbbcc') == 2, 'wrong result'
    assert solution.minDeletions('ceabaacb') == 2, 'wrong result'


if __name__ == '__main__':
    test_min_deletions()
