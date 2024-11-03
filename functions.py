

TODO_FILE_PATH = "todos.txt"


def read_todos(file_path=TODO_FILE_PATH):
    with open(file_path, "r") as local_file:
        todos_local=local_file.readlines()
    return todos_local


def write_todos(todos_arg, file_path=TODO_FILE_PATH):
    with open(file_path, "w") as file:
        file.writelines(todos_arg)


