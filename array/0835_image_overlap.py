class Solution:
    def largestOverlap(self, img1: list[list[int]], img2: list[list[int]]) -> int:
        n = len(img1)
        res = 0
        for dx in range(1 - n, n):
            for dy in range(1 - n, n):
                cnt = 0
                for i in range(max(-dx, 0), min(n - dx, n)):
                    for j in range(max(-dy, 0), min(n - dy, n)):
                        cnt += img1[i][j] * img2[i + dx][j + dy]
                res = max(res, cnt)
        return res


def test_largest_overlap():
    solution = Solution()
    assert solution.largestOverlap([[1, 1, 0], [0, 1, 0], [0, 1, 0]],
                                   img2=[[0, 0, 0], [0, 1, 1], [0, 0, 1]]) == 3, 'wrong result'
    assert solution.largestOverlap([[1]], img2=[[1]]) == 1, 'wrong result'
    assert solution.largestOverlap([[0]], img2=[[0]]) == 0, 'wrong result'


if __name__ == '__main__':
    test_largest_overlap()
