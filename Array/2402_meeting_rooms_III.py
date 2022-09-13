from typing import List
from heapq import heapify, heappush, heappop


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # 可以使用的房间号
        ready = [x for x in range(n)]
        # 正在使用的房间，元素[end_time, room_index]
        rooms = list()
        heapify(ready)
        res = [0] * n
        for start, end in sorted(meetings):
            while rooms and rooms[0][0] <= start:
                end_time, room_index = heappop(rooms)
                heappush(ready, room_index)
            if ready:
                room_index = heappop(ready)
                heappush(rooms, [end, room_index])
            else:
                end_time, room_index = heappop(rooms)
                heappush(rooms, [end_time + end - start, room_index])
            res[room_index] += 1
        return res.index(max(res))


def test_most_booked():
    solution = Solution()
    assert solution.mostBooked(2, [[0, 10], [1, 5], [2, 7], [3, 4]]) == 0, 'wrong result'
    assert solution.mostBooked(3, [[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]]) == 1, 'wrong result'


if __name__ == '__main__':
    test_most_booked()

