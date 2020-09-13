from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        nums = []
        cur = head
        while cur:
            nums.append(cur.val)
            cur = cur.next

        res = [0] * len(nums)
        stk = []
        for i in range(len(nums)):
            while stk and nums[stk[-1]] < nums[i]:
                tmp = stk.pop()
                res[tmp] = nums[i]
            stk.append(i)

        return res


def generate_linklist_by_nums(nums: List[int]):
    if not nums:
        return None
    cur = head = ListNode(nums[0])
    for i in range(1, len(nums)):
        cur.next = ListNode(nums[i])
        cur = cur.next

    return head


def test_next_larger_nodes():
    solution = Solution()

    nums1 = [2, 1, 5]
    print(solution.nextLargerNodes(generate_linklist_by_nums(nums1)))

    nums2 = [2, 7, 4, 3, 5]
    print(solution.nextLargerNodes(generate_linklist_by_nums(nums2)))

    nums3 = [1, 7, 5, 1, 9, 2, 5, 1]
    print(solution.nextLargerNodes(generate_linklist_by_nums(nums3)))


if __name__ == '__main__':
    test_next_larger_nodes()




