class MergeSortTopDown:
    def __init__(self, arr):
        self.arr = arr
        # self.aux = ['' for _ in range(len(arr))]
        self.merge_sort(0, len(self.arr) - 1)

    def merge(self, lo, mid, hi):
        i, j = lo, mid + 1
        aux = self.arr[lo: hi+1]
        # for k in range(lo, hi + 1):
        #     self.aux[k] = self.arr[k]

        for k in range(lo, hi + 1):
            if i > mid:
                self.arr[k] = aux[j - lo]
                j += 1
            elif j > hi:
                self.arr[k] = aux[i - lo]
                i += 1
            elif aux[i - lo] > aux[j - lo]:
                self.arr[k] = aux[j - lo]
                j += 1
            else:
                self.arr[k] = aux[i - lo]
                i += 1

    def merge_sort(self, lo, hi):
        if lo >= hi:
            return

        mid = lo + (hi - lo) // 2
        self.merge_sort(lo, mid)
        self.merge_sort(mid + 1, hi)
        self.merge(lo, mid, hi)


# 1. 对于小规模的数据排序，使用插入排序
# 2. 如果arr[mid] <= arr[mid + 1], 无须merge，直接拼接
class MergeSortTopDownAdvanced:
    def __init__(self, arr):
        self.arr = arr
        self.sort(0, len(arr) - 1)

    def sort(self, lo, hi):
        if lo >= hi:
            return

        mid = lo + (hi - lo) // 2
        self.sort(lo, mid)
        self.sort(mid + 1, hi)

        if self.arr[mid] > self.arr[mid + 1]:
            self.merge(lo, mid, hi)

    def merge(self, lo, mid, hi):
        i, j = lo, mid + 1
        aux = self.arr[lo: hi + 1]

        for k in range(lo, hi + 1):
            if i > mid:
                self.arr[k] = aux[j - lo]
                j += 1
            elif j > hi:
                self.arr[k] = aux[i - lo]
                i += 1
            elif aux[i - lo] > aux[j - lo]:
                self.arr[k] = aux[j - lo]
                j += 1
            else:
                self.arr[k] = aux[i - lo]
                i += 1


def test_merge_sort():
    a = ['M', 'E', 'R', 'G', 'E', 'S', 'O', 'R', 'T', 'E', 'X', 'A', 'M', 'P', 'L', 'E']
    print(a)
    merge_sort = MergeSortTopDownAdvanced(a)
    print(merge_sort.arr)


if __name__ == '__main__':
    test_merge_sort()
