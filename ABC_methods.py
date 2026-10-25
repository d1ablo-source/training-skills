from abc import ABC, abstractmethod


class UserRepository(ABC):
    @abstractmethod
    def save(self, name):
        ...

    @abstractmethod
    def get(self, index):
        ...

class MemoryUserRepository(UserRepository):
    def __init__(self):
        self.users = []

    def save(self, name):
        self.users.append(name)

    def get(self, index):
        return self.users[index]
        

repo = MemoryUserRepository()
repo.save("Аня")
print(repo.get(0))   # Аня


class Storage(ABC):
    @abstractmethod
    def save(self, key, value):
        ...

    @abstractmethod
    def load(self, key):
        ...

class MemoryStorage(Storage):
    def __init__(self):
        self.data = {}

    def save(self, key, value):
        self.data[key] = value

    def load(self, key):
        if key not in self.data:
            raise KeyError(f"Ключ {key!r} не найден")
        return self.data[key]

    
class LoggingStorage(Storage):
    def __init__(self):
        self.data = {}

    def save(self, key, value):
        print(f"saved: {key}")
        self.data[key] = value

    def load(self, key):
        if key not in self.data:
            raise KeyError(f"Ключ {key!r} не найден")
        return self.data[key]    

s = LoggingStorage()
s.save("a", 1)
print(s.load("a"))