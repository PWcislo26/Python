import magazine.utils

class Order:

    def __init__(self, products, price, client):
        self._products = products
        self._price = price
        self._client = client

    def __str__(self) -> str:
        return f"{self._client} ordered {self._products}"