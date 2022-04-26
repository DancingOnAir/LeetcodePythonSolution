from operator import add, mul
from functools import partial


# list operation
class Fancy1:
    def __init__(self):
        self.arr = list()

    def append(self, val: int) -> None:
        self.arr.append(val)

    def addAll(self, inc: int) -> None:
        self.arr = list(map(partial(add, inc), self.arr))

    def multAll(self, m: int) -> None:
        self.arr = list(map(partial(mul, m), self.arr))

    def getIndex(self, idx: int) -> int:
        if idx < len(self.arr):
            return self.arr[idx] % (10 ** 9 + 7)
        return -1


# math: Fermat's little theorem
class Fancy2:
    def __init__(self):
        self.data = list()
        self.csum = [0]
        self.cmul = [1]
        self.mod = 10 ** 9 + 7

    def append(self, val: int) -> None:
        self.data.append(val)
        self.csum.append(self.csum[-1])
        self.cmul.append(self.cmul[-1])

    def addAll(self, inc: int) -> None:
        self.csum[-1] += inc

    def multAll(self, m: int) -> None:
        self.cmul[-1] *= m
        self.cmul[-1] %= self.mod

        self.csum[-1] *= m
        self.csum[-1] %= self.mod

    def getIndex(self, idx: int) -> int:
        if idx < len(self.data):
            # Fermat's little theorem states that if p is a prime number, then for any integer a,
            # the number a^p − a is an integer multiple of p, i.e. a^p = a (mod p).
            # In this application, we need a^(p-2) = a^-1 (mod p) where p is 1_000_000_007.
            # ratio = self.cmul[-1] * pow(self.cmul[idx], -1, self.mod)
            ratio = self.cmul[-1] * pow(self.cmul[idx], self.mod - 2, self.mod)
            return (self.csum[-1] + (self.data[idx] - self.csum[idx]) * ratio) % self.mod
        return -1


# math: functional computing:
# Since we only add and multiply, the transformation is a linear function x ↦ ax + b, defined by a and b.
# When we add, we change it to (ax + b) + inc = ax + (b+inc), i.e., we just add inc to b.
# When we multiply, we change it to (ax + b) * m = (am)x + (bm), i.e., we multiply both a and b by m.
class Fancy3:
    def __init__(self):
        self.data = list()
        self.add = 0
        self.mul = 1
        self.mod = 10 ** 9 + 7

    def append(self, val: int) -> None:
        self.data.append((val - self.add) * pow(self.mul, -1, self.mod))

    def addAll(self, inc: int) -> None:
        self.add += inc

    def multAll(self, m: int) -> None:
        self.add = self.add * m % self.mod
        self.mul = self.mul * m % self.mod

    def getIndex(self, idx: int) -> int:
        if idx < len(self.data):
            return (self.data[idx] * self.mul + self.add) % self.mod
        return -1


# segment tree
class Fancy:
    def __init__(self):
        self.n = 10 ** 5 + 1
        self.mod = 10 ** 9 + 7
        self.sz = 0
        self.tree = [0] * (self.n << 2)
        self.param_a = [1] * (self.n << 2)
        self.param_b = [0] * (self.n << 2)

    def update(self, tree_idx, l, r, xl, xr, val):
        if xl > r or xr < l:
            return

        if l >= xl and r <= xr:
            if val > 0:
                self.tree[tree_idx] = (self.tree[tree_idx] + val) % self.mod
                self.param_b[tree_idx] = (self.param_b[tree_idx] + val) % self.mod
            else:
                self.tree[tree_idx] = (self.tree[tree_idx] * -val) % self.mod
                self.param_a[tree_idx] = (self.param_a[tree_idx] * -val) % self.mod
                self.param_b[tree_idx] = (self.param_b[tree_idx] * -val) % self.mod
        else:
            self.push_down(tree_idx, l, r)
            mid = (l + r) >> 1
            self.update(tree_idx << 1, l, mid, xl, xr, val)
            self.update(tree_idx << 1 | 1, mid + 1, r, xl, xr, val)

    def query(self, tree_idx, l, r, xl, xr):
        if xl > r or xr < l:
            return 0
        if xl == l and xr == r:
            return self.tree[tree_idx]

        self.push_down(tree_idx, l, r)
        mid = (l + r) >> 1
        return self.query(tree_idx << 1, l, mid, xl, xr) + self.query(tree_idx << 1 | 1, mid + 1, r, xl, xr)

    def push_down(self, tree_idx, l, r):
        if l < r and (self.param_a[tree_idx] > 1 or self.param_b[tree_idx] > 0):
            self.tree[tree_idx << 1] = (self.tree[tree_idx << 1] * self.param_a[tree_idx] + self.param_b[tree_idx]) % self.mod
            self.param_a[tree_idx << 1] = (self.param_a[tree_idx << 1] * self.param_a[tree_idx]) % self.mod
            self.param_b[tree_idx << 1] = (self.param_b[tree_idx << 1] * self.param_a[tree_idx] + self.param_b[tree_idx]) % self.mod

            self.tree[tree_idx << 1 | 1] = (self.tree[tree_idx << 1 | 1] * self.param_a[tree_idx] + self.param_b[tree_idx]) % self.mod
            self.param_a[tree_idx << 1 | 1] = (self.param_a[tree_idx << 1 | 1] * self.param_a[tree_idx]) % self.mod
            self.param_b[tree_idx << 1 | 1] = (self.param_b[tree_idx << 1 | 1] * self.param_a[tree_idx] + self.param_b[tree_idx]) % self.mod

            self.param_a[tree_idx] = 1
            self.param_b[tree_idx] = 0
        pass

    def append(self, val: int) -> None:
        self.update(1, 0, self.n - 1, self.sz, self.sz, val)
        self.sz += 1

    def addAll(self, inc: int) -> None:
        self.update(1, 0, self.n - 1, 0, self.sz - 1, inc)

    def multAll(self, m: int) -> None:
        self.update(1, 0, self.n - 1, 0, self.sz - 1, -m)

    def getIndex(self, idx: int) -> int:
        if idx < self.sz:
            return self.query(1, 0, self.n - 1, idx, idx)
        return -1


def test_fancy():
    obj = Fancy()

    obj.append(2)
    obj.addAll(3)
    obj.append(7)
    obj.multAll(2)
    assert obj.getIndex(0) == 10, 'wrong result'

    obj.addAll(3)
    obj.append(10)
    obj.multAll(2)
    assert obj.getIndex(0) == 26, 'wrong result'
    assert obj.getIndex(1) == 34, 'wrong result'
    assert obj.getIndex(2) == 20, 'wrong result'


if __name__ == '__main__':
    test_fancy()
