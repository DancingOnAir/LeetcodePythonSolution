from collections import defaultdict


class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        cnt = {}
        i = 0
        for j, x in enumerate(fruits):
            cnt[x] = cnt.get(x, 0) + 1
            if len(cnt) > 2:
                cnt[fruits[i]] -= 1
                if cnt[fruits[i]] == 0:
                    del cnt[fruits[i]]
                i += 1
        return j - i + 1

    def totalFruit1(self, fruits: list[int]) -> int:
        res = left = tot = 0
        m = defaultdict(int)

        for right, x in enumerate(fruits):
            m[x] += 1
            tot += 1
            if len(m) < 3:
                res = max(res, tot)
            while left <= right and len(m) > 2:
                tot -= 1
                m[fruits[left]] -= 1
                if m[fruits[left]] == 0:
                    del m[fruits[left]]
                left += 1
        return res


def test_total_fruit():
    solution = Solution()
    assert solution.totalFruit([1, 2, 1]) == 3, 'wrong result'
    assert solution.totalFruit([0, 1, 2, 2]) == 3, 'wrong result'
    assert solution.totalFruit([1, 2, 3, 2, 2]) == 4, 'wrong result'


if __name__ == '__main__':
    test_total_fruit()
