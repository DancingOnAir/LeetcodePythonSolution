from collections import defaultdict


class Solution:
    def countStaircase(self, nums: list[int]) -> int:
        pos = defaultdict(list)
        firsts = []
        n = len(nums)
        res = 0

        for i in range(n - 1, -1, -1):
            x = nums[i]
            pos[x].append(i)

            if x in firsts:
                firsts.remove(x)
            firsts.insert(0, x)

            m = len(firsts)
            if m * (m + 1) // 2 > n:
                firsts.pop()

            mx, mn = 0, n
            # 子数组右开端点
            r = i
            for k, y in enumerate(firsts, 1):
                r += k
                ps = pos[y]
                if k > len(ps):
                    break

                mx = max(mx, ps[-k])
                if k < len(ps):
                    mn = min(mn, ps[-1 - k])
                if mx >= mn or r > mn:
                    break
                if mx < r:
                    res += 1
        return res


def test_count_staircase():
    solution = Solution()
    assert solution.countStaircase([5, 8, 8, 2, 2, 2]) == 9, 'wrong result'
    assert solution.countStaircase([6, 6, 9, 9]) == 5, 'wrong result'
    assert solution.countStaircase([2, 3, 4, 4, 3, 4]) == 8, 'wrong result'


if __name__ == '__main__':
    test_count_staircase()
