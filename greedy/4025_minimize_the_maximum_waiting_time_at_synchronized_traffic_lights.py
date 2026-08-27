from bisect import bisect_right


class Solution:
    def minPenalty(self, period: int, lights: list[int], arrivalTime: list[int]) -> int:
        max_green = max(lights)
        min_red = period
        for t in arrivalTime:
            r = t % period
            if max_green <= r < min_red:
                min_red = r
                if min_red == max_green:
                    break
        return period - min_red

    def minPenalty1(self, period: int, lights: list[int], arrivalTime: list[int]) -> int:
        lights.sort()
        n = len(lights)
        res = []
        for t in arrivalTime:
            r = t % period
            i = bisect_right(lights, r)
            res.append(0 if i < n else period-r)
        return max(res)


def test_min_penalty():
    solution = Solution()
    assert solution.minPenalty(8, lights = [2,3], arrivalTime = [2,5,8,11]) == 5, 'wrong result'
    assert solution.minPenalty(10, lights = [3,6,8], arrivalTime = [4,9,15]) == 1, 'wrong result'
    assert solution.minPenalty(5, lights = [2], arrivalTime = [2,3,4,5,6]) == 3, 'wrong result'


if __name__ == '__main__':
    test_min_penalty()
