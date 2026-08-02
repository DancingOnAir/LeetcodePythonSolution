class Solution:
    def aggregateTimeSeries(self, series1: list[list[int]], series2: list[list[int]]) -> list[list[int]]:
        res = []
        i = j = 0
        m, n = len(series1), len(series2)
        while i < m and j < n:
            t1, t2 = series1[i][0], series2[j][0]
            val = series1[i][1] + series2[j][1]
            if t1 < t2:
                res.append([t1, val])
                i += 1
            elif t1 > t2:
                res.append([t2, val])
                j += 1
            else:
                res.append([t1, val])
                i += 1
                j += 1

        res += series1[i:]
        res += series2[j:]
        return res


def test_aggregate_time_series():
    solution = Solution()
    assert solution.aggregateTimeSeries([[1, 3], [4, 1]], series2=[[2, 2], [5, 2]]) == [[1, 5], [2, 3], [4, 3],
                                                                                        [5, 2]], 'wrong result'
    assert solution.aggregateTimeSeries([[1, 5], [3, 1]], series2=[[2, 2]]) == [[1, 7], [2, 3], [3, 1]], 'wrong result'
    assert solution.aggregateTimeSeries([[1, 5]], series2=[[1000000000, 2]]) == [[1, 7],
                                                                                 [1000000000, 2]], 'wrong result'


if __name__ == '__main__':
    test_aggregate_time_series()
