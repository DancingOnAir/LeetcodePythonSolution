from typing import List


class Solution:
    def resultGrid(self, image: List[List[int]], threshold: int) -> List[List[int]]:
        
        pass


def test_result_grid():
    solution = Solution()
    assert solution.resultGrid([[5, 6, 7, 10], [8, 9, 10, 10], [11, 12, 13, 10]], 3) == [[9, 9, 9, 9], [9, 9, 9, 9],
                                                                                         [9, 9, 9, 9]], 'wrong result'
    assert solution.resultGrid([[10, 20, 30], [15, 25, 35], [20, 30, 40], [25, 35, 45]], 12) == [[25, 25, 25],
                                                                                                 [27, 27, 27],
                                                                                                 [27, 27, 27], [30, 30,
                                                                                                                30]], 'wrong result'
    assert solution.resultGrid([[5, 6, 7], [8, 9, 10], [11, 12, 13]], 1) == [[5, 6, 7], [8, 9, 10],
                                                                             [11, 12, 13]], 'wrong result'


if __name__ == '__main__':
    test_result_grid()
