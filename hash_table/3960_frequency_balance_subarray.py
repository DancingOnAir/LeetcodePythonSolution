from collections import defaultdict


class Solution:
    def getLength(self, nums: list[int]) -> int:
        n = len(nums)
        if len(set(nums)) == 1:
            return n

        res = same = 0
        for i, x in enumerate(nums):
            same += 1
            if i == n - 1 or x != nums[i + 1]:
                res = max(res, same)
                same = 0

        for i in range(n):
            if n - i <= res:
                break

            cnt = defaultdict(int)
            cc = defaultdict(int)

            for j in range(i, n):
                x = nums[j]
                c = cnt[x]

                if c > 0:
                    cc[c] -= 1
                    if cc[c] == 0:
                        del cc[c]
                cnt[x] += 1
                cc[cnt[x]] += 1

                if len(cc) == 2:
                    c1, c2 = sorted(cc)
                    if c1 * 2 == c2:
                        res = max(res, j - i + 1)
        return res


def test_get_length():
    solution = Solution()
    assert solution.getLength([1, 2, 2, 1, 2, 3, 3, 3]) == 5, 'wrong answer'
    assert solution.getLength([5, 5, 5, 5]) == 4, 'wrong answer'
    assert solution.getLength([1, 2, 3, 4]) == 1, 'wrong answer'


if __name__ == '__main__':
    test_get_length()
