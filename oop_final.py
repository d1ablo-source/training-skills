from dataclasses import dataclass


@dataclass(frozen=True)
class Money:
    amount: float
    currency: str = "USD"

    def __post_init__(self):
        if self.amount < 0:
            raise ValueError("Сумма не может быть отрицательной")
        if not isinstance(self.currency, str) or len(self.currency) != 3:
            raise ValueError("Валюта должна быть строкой из 3 букв")

    def __add__(self, other):
        if self.currency != other.currency:
            raise ValueError(f"Нельзя сложить {self.currency} и {other.currency}")
        return Money(self.amount + other.amount, self.currency)


@dataclass(frozen=True)
class Item:
    name: str
    price: Money

    def __post_init__(self):
        if not self.name.strip():
            raise ValueError("Имя не может быть пустым")

class Cart:
    def __init__(self, items=None):
        self.items = list(items or [])

    def __len__(self):
        return len(self.items)

    def __iter__(self):
        return iter(self.items)

    def __repr__(self):
        return f"Cart({self.items!r})"

    def __add__(self, other):
        return Cart(self.items + other.items)

    def total(self):
        if not self.items:
            raise ValueError("Корзина пуста")
        result = self.items[0].price
        for item in self.items[1:]:
            result += item.price
        return result


c1 = Cart([Item("Книга", Money(500, "USD"))])
c2 = Cart([Item("Ручка", Money(5, "USD"))])
print(len(c1 + c2))
print((c1 + c2).total())