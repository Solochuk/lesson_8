import json


def main():
    while True:
        print("Список можливих дій:\n"
              " 1. Читати список завдань.\n"
              " 2. Додати нове завдання.\n"
              " 3. Видалити задання за номером.\n"
              " 4. Вийти."
              )

        action = input("Оберіть дію зі списку і напишить її номер: ")
        if action == "1":
            read()
        elif action == "2":
            write()
        elif action == "3":
            delete()
        elif action == "4":
            break
        else:
            print("Оберіть коректну дію!\n")


def read():
    try:
        with open("ToDoList.json", "r") as file:
            tasks = json.load(file)
            for task in tasks:
                print(f" №: {task['id']}\n"
                      f" Назва завдання: {task['name']}\n"
                      f" Опис завдання: {task['description']}\n"
                      )
    except FileNotFoundError:
        print("Файл зі списком не знайдено!\n")


def write():
    try:
        with open("ToDoList.json", "r") as file:
            tasks = json.load(file)

    except FileNotFoundError:
        tasks = []


    if not tasks:
        new_task_id = 1
    else:
        new_task_id = max(task["id"] for task in tasks) + 1

    new_task_name = input(" Введіть назву завдання: ")
    new_task_description = input(" Введіть опис завданя: ")

    new_task = {
        "id": new_task_id,
        "name": new_task_name,
        "description": new_task_description
    }

    with open("ToDoList.json", "w") as file:
        tasks.append(new_task)
        json.dump(tasks, file)

    print(f"Завдання ({new_task_name}) успішно додано!\n")


def delete():
    try:
        with open("ToDoList.json", "r") as file:
            tasks = json.load(file)
        task_id = input(" Введіть номер завдання для видалення:")

        if task_id in tasks:
            tasks = [task for task in tasks if task["id"] != int(task_id)]

            with open("ToDoList.json", "w") as file:
                json.dump(tasks, file)

                print(f"Задання з номером {task_id} успішно видалено!\n")
        else:
            print("Такого задання не існує!!!\n")
    except FileNotFoundError:
        print("Файл зі списком не знайдено!\n")


if __name__ == '__main__':
    main()
