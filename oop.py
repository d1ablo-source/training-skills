from dataclasses import dataclass


@dataclass(frozen=True)
class Money:
    amount: float
    currency: str = "USD"

    def __add__(self, other):
        if self.currency != other.currency:
            raise ValueError(f"Нельязя складывать {self.currency} и {other.currency}")
        return Money(self.amount + other.amount, self.currency)

    
        
usd = Money(100, "USD")
rub = Money(10000, "RUB")
usd2 = Money(123, "USD")

print(usd)
print(usd.currency == rub.currency)

print(usd + usd2)


class Playlist:
    def __init__(self, songs=None):
        self.songs = list(songs or []) #list(songs or []) значит: «если songs не передали, возьми пустой список; иначе сделай копию переданного»

    def __len__(self):
        return len(self.songs)

    def __repr__(self):
        return f"Playlist({self.songs!r})"

    def __iter__(self):
        return iter(self.songs)

    def __contains__(self, song):
        return song in self.songs

    def __add__(self, other):
        return Playlist(self.songs + other.songs)

    def __getitem__(self, index):
        return self.songs[index]
    
p1 = Playlist(["A", "B"])
p2 = Playlist(["C"])

print(p1[0])
print(p1[1])
print(p1 + p2)
print(len(p1))


class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def celsius(self):
        return self._celsius
    
    @property
    def fahrenheit(self):
        return self.celsius * 9 / 5 + 32

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Не может быть ниже -273.15")
        self._celsius = value

t = Temperature(100)
print(t.fahrenheit)
t.celsius = 0
print(t.fahrenheit)
