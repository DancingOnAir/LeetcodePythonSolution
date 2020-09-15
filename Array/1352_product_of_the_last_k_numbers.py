from typing import List


class ProductOfNumbers:
    def __init__(self):
        self.products = [1]
        pass

    def add(self, num: int) -> None:
        if not num:
            self.products = [1]
        else:
            self.products.append(self.products[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.products):
            return 0

        return int(self.products[-1] / self.products[-k - 1])


def test_product_of_numbers():
    product_of_numbers = ProductOfNumbers()
    product_of_numbers.add(3)
    product_of_numbers.add(0)
    product_of_numbers.add(2)
    product_of_numbers.add(5)
    product_of_numbers.add(4)
    print(product_of_numbers.getProduct(2))
    print(product_of_numbers.getProduct(3))
    print(product_of_numbers.getProduct(4))
    product_of_numbers.add(8)
    print(product_of_numbers.getProduct(2))


if __name__ == '__main__':
    test_product_of_numbers()
