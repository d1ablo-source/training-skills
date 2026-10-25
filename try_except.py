from pathlib import Path


class Door:
    def __enter__(self):
        print("открыли")
        return self

    def __exit__(self, exc_type, exc, tb):
        print("закрыли")
        return False

try:
    with Door():
        print("внутри")
        raise ValueError("ой")
        print("не дойдём")
except ValueError:
    print("поймали")




p = Path("data") / "report.txt"
print(p.name)
print(p.suffix)
print(p.parent)
print("data" / Path("a.txt"))