from typing import List


class OrderedStream:
    def __init__(self, n: int):
        self.ptr = 1
        self.mp = dict()
        pass

    def insert(self, id: int, value: str) -> List[str]:
        self.mp[id] = [value] + self.mp.get(id + 1, [])
        pre_id = id
        while pre_id > 1:
            pre_id -= 1
            if pre_id in self.mp:
                self.mp[pre_id] = [self.mp[pre_id][0]] + self.mp[pre_id + 1]
            else:
                break

        if self.ptr == id:
            self.ptr += len(self.mp[id])
            return self.mp[id]

        return []


def test_ordered_stream():
    obj = OrderedStream(5)
    assert obj.insert(3, "ccccc") == [], "wrong result"
    assert obj.insert(1, "aaaaa") == ["aaaaa"], "wrong result"
    assert obj.insert(2, "bbbbb") == ["bbbbb", "ccccc"], "wrong result"
    assert obj.insert(5, "eeeee") == [], "wrong result"
    assert obj.insert(4, "ddddd") == ["ddddd", "eeeee"], "wrong result"


if __name__ == '__main__':
    test_ordered_stream()
