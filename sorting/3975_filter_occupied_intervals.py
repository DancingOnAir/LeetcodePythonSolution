class Solution:
    def filterOccupiedIntervals(self, occupiedIntervals: list[list[int]], freeStart: int, freeEnd: int) -> list[list[int]]:
        occupiedIntervals.sort(key=lambda x: x[0])
        res = []

        def add(l: int, r: int) -> None:
            if l > freeEnd or r < freeStart:
                res.append([l, r])
                return
            if l < freeStart:
                res.append([l, freeStart - 1])
            if r > freeEnd:
                res.append([freeEnd + 1, r])

        left, max_right = occupiedIntervals[0]
        for l, r in occupiedIntervals[1:]:
            if l - 1 > max_right:
                add(left, max_right)
                left = l
            max_right = max(max_right, r)
        add(left, max_right)
        return res


def test_filter_occupied_intervals():
    solution = Solution()
    assert solution.filterOccupiedIntervals([[2,6],[4,8],[10,10],[10,12],[14,16]], 7, 11) == [[2,6],[12,12],[14,16]], 'wrong result'
    assert solution.filterOccupiedIntervals([[1,5],[2,3]], 3, 8) == [[1,2]], 'wrong result'


if __name__ == '__main__':
    test_filter_occupied_intervals()
