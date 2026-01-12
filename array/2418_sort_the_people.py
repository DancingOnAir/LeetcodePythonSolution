from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [b for _, b in sorted(zip(heights, names), key=lambda x: -x[0])]

    def sortPeople1(self, names: List[str], heights: List[int]) -> List[str]:
        return [names[i] for _, i in sorted({val: i for i, val in enumerate(heights)}.items(), key=lambda x: -x[0])]


def test_sort_people():
    solution = Solution()
    assert solution.sortPeople(["Mary", "John", "Emma"], [180, 165, 170]) == ["Mary", "Emma", "John"], 'wrong result'
    assert solution.sortPeople(["Alice", "Bob", "Bob"], [155, 185, 150]) == ["Bob", "Alice", "Bob"], 'wrong result'


if __name__ == '__main__':
    test_sort_people()

