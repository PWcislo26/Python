import magazine.utils as util

class Product:

    def __init__(self, name, price, details):
        self._name = name
        self._price = price
        self._details = details

    def __str__(self) -> str:
        return f"Product {self._name} costs {self._price}"


if __name__ == "__main__":
    util.util_test()