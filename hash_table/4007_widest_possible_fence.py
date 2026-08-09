from collections import Counter


class Solution:
    def maximumWidth(self, planks: list[int]) -> int:
        cnt = Counter(planks)

        res = 0
        cnt_pair = Counter()
        for x, v1 in cnt.items():
            cnt_pair[x] += v1
            cnt_pair[x * 2] += v1 // 2
            for y, v2 in cnt.items():
                if y > x:
                    cnt_pair[x + y] += min(v1, v2)
        return max(cnt_pair.values())


def test_maximum_width():
    solution = Solution()
    assert solution.maximumWidth([1, 3, 2, 5, 7, 5, 4, 2, 1]) == 4, 'wrong result'
    assert solution.maximumWidth([2, 3, 7]) == 1, 'wrong result'


if __name__ == '__main__':
    test_maximum_width()
