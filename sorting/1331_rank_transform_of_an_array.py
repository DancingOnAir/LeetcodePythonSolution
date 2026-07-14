from collections import Counter


class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        sorted_unique = sorted(list(set(arr)))
        rank = {}
        for i, x in enumerate(sorted_unique, 1):
            rank[x] = i
        return [rank[x] for x in arr]

    def arrayRankTransform1(self, arr: list[int]) -> list[int]:
        cnt = Counter(arr)
        sorted_keys = sorted(cnt.keys())
        cnt.clear()
        for i, x in enumerate(sorted_keys):
            cnt[x] = i + 1
        res = []
        for x in arr:
            res.append(cnt.get(x, 0))
        return res


def test_array_rank_transform():
    solution = Solution()
    assert solution.arrayRankTransform([40,10,20,30]) == [4,1,2,3], 'wrong result'
    assert solution.arrayRankTransform([100,100,100]) == [1,1,1], 'wrong result'
    assert solution.arrayRankTransform([37,12,28,9,100,56,80,5,12]) == [5,3,4,2,8,6,7,1,3], 'wrong result'


if __name__ == '__main__':
    test_array_rank_transform()

