from typing import List
from heapq import heapify, heappush, heappop


class Solution:
    def boxDelivering(self, boxes: List[List[int]], portsCount: int, maxBoxes: int, maxWeight: int) -> int:
        # heapify(boxes)
        boxes.reverse()
        res = 0
        ports = list()
        while len(boxes) > 0:
            num_boxes = weight = 0

            while num_boxes <= maxBoxes and weight <= maxWeight:
                box = boxes[-1]
                if num_boxes + 1 > maxBoxes or weight + box[1] > maxWeight:
                    break

                num_boxes += 1
                weight += box[1]
                boxes.pop()

                if ports[-1] != box[0]:
                    ports.append(box[0])

        return res


def test_box_delivering():
    solution = Solution()
    assert solution.boxDelivering([[1, 1], [2, 1], [1, 1]], 2, 3, 3) == 4, 'wrong result'
    assert solution.boxDelivering([[1, 2], [3, 3], [3, 1], [3, 1], [2, 4]], 3, 3, 6) == 6, 'wrong result'
    assert solution.boxDelivering([[1, 4], [1, 2], [2, 1], [2, 1], [3, 2], [3, 4]], 3, 6, 7) == 6, 'wrong result'


if __name__ == '__main__':
    test_box_delivering()

