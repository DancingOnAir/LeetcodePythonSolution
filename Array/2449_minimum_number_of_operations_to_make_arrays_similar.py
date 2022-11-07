from typing import List


class Solution:
    # +2，-2的1个操作后，原数的奇偶性不变
    # 如果对整个nums, target排序直接比较，测试2会错误
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0

        nums.sort(key=lambda x: (x & 1, x))
        target.sort(key=lambda x: (x & 1, x))
        return sum(abs(a - b) for a, b in zip(nums, target)) // 4


def test_make_similar():
    solution = Solution()
    assert solution.makeSimilar([8, 12, 6], [2, 14, 10]) == 2, 'wrong result'
    assert solution.makeSimilar([1, 2, 5], [4, 1, 3]) == 1, 'wrong result'


if __name__ == '__main__':
    test_make_similar()
