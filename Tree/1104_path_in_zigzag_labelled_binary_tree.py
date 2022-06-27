from typing import List
from math import log2

class Solution:
    # len(bin(x)) - 4 is the level. eg len(bin(2)) = 0
    # the smallest and biggest together we get 3 * 2 ** (len(bin(x)) - 4) - 1
    # node + mirrored_node = smallest + biggest
    # -> zigzag_parent = smallest + biggest - nonzigzag_parent
    def pathInZigZagTree(self, label: int) -> List[int]:
        level = int(log2(label))
        nonzigzag_parent = 3 * 2 ** level - 1 - label

        res = list()
        while label:
            res.append(label)
            label //= 2
            nonzigzag_parent //= 2
            label, nonzigzag_parent = nonzigzag_parent, label
        return res[::-1]

    # straight forward
    def pathInZigZagTree1(self, label: int) -> List[int]:
        level = 0
        label_idx = -1
        arr = list()
        while 2 ** level <= label:
            cur = list()
            for num in range(2 ** level, 2 ** (level + 1)):
                cur.append(num)
                if num == label:
                    label_idx = len(cur) - 1
            level += 1
            if level & 1:
                label_idx += len(arr)
                arr.extend(cur)
            else:
                label_idx = len(arr) + len(cur) - label_idx - 1
                arr.extend(cur[::-1])

        res = list()
        while label_idx > 0:
            res.append(arr[label_idx])
            label_idx = (label_idx - 1) // 2
        res.append(arr[0])
        return res[::-1]


def test_path_in_zigzag_tree():
    solution = Solution()
    assert solution.pathInZigZagTree(14) == [1, 3, 4, 14], 'wrong result'
    assert solution.pathInZigZagTree(26) == [1, 2, 6, 10, 26], 'wrong result'


if __name__ == '__main__':
    test_path_in_zigzag_tree()
