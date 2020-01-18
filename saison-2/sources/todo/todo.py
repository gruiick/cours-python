class Todo:
    def __init__(self, contents, done):
        self.contents = contents
        self.done = done


class TodoList:
    def __init__(self):
        self.todos = []

    def add(self, contenu):
        self.todos.append(Todo(contenu, False))

    def mark_as_done(self, i):
        self.todos[i - 1].done = True

    def mark_as_not_done(self, i):
        self.todos[i - 1].done = False

    def show(self):
        if not self.todos:
            print("nothing yet")
        i = 1
        for todo in self.todos:
            if todo.done:
                print(i, "[x]", todo.contents)
            else:
                print(i, "[ ]", todo.contents)
            i += 1


def parse_answer(answer):
    if answer.startswith("+ "):
        return "add", answer[2:]
    if answer.startswith("- "):
        return "remove", int(answer[2:])
    if answer.startswith("x "):
        return "done", int(answer[2:])
    if answer.startswith("o "):
        return "undo", int(answer[2:])
    return "error", ""


def main():
    todo_list = TodoList()
    while True:
        todo_list.show()
        answer = input("+ / x / o ?\n")
        command, arg = parse_answer(answer)
        if command == "add":
            todo_list.add(arg)
        if command == "done":
            todo_list.mark_as_done(arg)
        if command == "undo":
            todo_list.mark_as_not_done(arg)
        if command == "error":
            print("error")


if __name__ == "__main__":
    main()
