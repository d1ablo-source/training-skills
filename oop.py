class Money:

    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency


    def __repr__(self):
        return f"amount: {self.amount}, currency: {self.currency}"
    
    
    def __eq__(self, other):
        return self.currency == other.currency


    def __add__(self, other):
        return Money(self.amount + other.amount, self.currency)
        
usd = Money(100, "USD")
rub = Money(10000, "RUB")
usd2 = Money(123, "USD")

print(usd)
print(usd == rub)
if usd == usd2:
    print(usd + usd2)
else:
    raise ValueError
