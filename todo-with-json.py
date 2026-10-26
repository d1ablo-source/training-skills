from dataclasses import dataclass, asdict
from pathlib import Path
import json


@dataclass
class Task:
    title: str
    done: bool = False

class TodoError(Exception):
    pass

class FileNotFoundError(Exception):
    pass


class TodoList:
    def __init__(self):
        self.tasks = []

    def add(self, title):
        self.tasks.append(Task(title))      # создать Task и положить в self.tasks

    def __len__(self):
        return len(self.tasks)

    def complete(self, index):
        if len(self.tasks) <= index or index < 0:
            raise TodoError(f"Нет задачи с номером {index}")
        self.tasks[index].done = True

    def save(self, path):
        data = [asdict(t) for t in self.tasks]
        text = json.dumps(data, ensure_ascii=False)
        Path(path).write_text(text, encoding="utf-8")

    def load(self, path):
        try:
            text = Path(path).read_text(encoding="utf-8")
        except FileNotFoundError:
            print("Файл не найден, начинаем с пустого списка")
            return
        data = json.loads(text)
        task = [Task(**d) for d in data]
        self.tasks = task


todo = TodoList()
todo.load("todo.json")

while True:
    line = input("> ")
    parts = line.split(maxsplit=1)
    command = parts[0]

    try:
        if command == "quit":
            break
        elif command == "add":
            todo.add(parts[1])
        elif command == "done":
            todo.complete(int(parts[1]))
        elif command == "list":
                for i, task in enumerate(todo.tasks):
                    print(i, task.title, task.done)
    except TodoError as e:
        print(f"Ошибка: {e}")
    except (ValueError, IndexError):
        print("Неверная команда")

todo.save("todo.json")

# todo = TodoList()
# todo.add("хлеб")
# todo.add("молоко")
# print(len(todo))
# print(todo.tasks)
# print(todo.tasks[1].done)

# todo = TodoList()
# todo.add("хлеб")
# todo.complete(0)
# todo.save("todo.json")
# print(Path("todo.json").read_text(encoding="utf-8"))

# todo = TodoList()
# todo.load("todo.json")
# print(len(todo))
# print(todo.tasks[0])
# print(todo.tasks[0].done)