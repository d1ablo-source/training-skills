from dataclasses import dataclass


@dataclass
class Money:
    amount: int | float
    currency: str = "USD"

    def __add__(self, other):
        return Money(self.amount + other.amount, self.currency)
        
usd = Money(100, "USD")
rub = Money(10000, "RUB")
usd2 = Money(123, "USD")

print(usd)
print(usd == rub)
if usd.currency == usd2.currency:
    print(usd + usd2)
else:
    raise ValueError
