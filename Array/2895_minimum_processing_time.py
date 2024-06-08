from typing import List


class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse=True)
        res = 0
        for i, x in enumerate(processorTime):
            for j in range(i * 4, i * 4 + 4):
                res = max(res, x + tasks[j])

        return res


def test_min_processing_time():
    solution = Solution()
    assert solution.minProcessingTime([8, 10], [2, 2, 3, 1, 8, 7, 4, 5]) == 16, 'wrong result'
    assert solution.minProcessingTime([10, 20], [2, 3, 1, 2, 5, 8, 4, 3]) == 23, 'wrong result'


if __name__ == '__main__':
    test_min_processing_time()
