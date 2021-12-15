import os
from typing import Dict, List
from datetime import datetime

Tasks = Dict[str, List[str]]
cache_file = 'cache.csv'


def add_task(tasks: Tasks, strdate: str, name: str, priority: int):
    if strdate not in tasks:
        tasks[strdate] = []
    tasks[strdate].insert(priority, name)


def delete_task(tasks: Tasks, strdate: str, name: str):
    tasks[strdate].remove(name)
    if len(tasks[strdate]) == 0:
        del tasks[strdate]


def print_tasks(tasks: Tasks, strdate: str):
    if strdate not in tasks:
        print("You have no tasks for today")
    else:
        print(f"Current tasks for {strdate}:")
        for task in tasks[strdate]:
            print(f"{strdate}  --- {task}")


def read_tasks() -> Tasks:
    if not os.path.isfile(cache_file):
        return dict()
    with open(cache_file, 'r') as file:
        lines = file.read().split('\n')[:-1]
        tasks = dict()
        for line in lines:
            sep_idx = line.index(':')
            date = line[:sep_idx]
            task_list = line[sep_idx + 1:]
            tasks[date] = task_list.split(';')
        return tasks


def write_tasks(tasks: Tasks):
    with open(cache_file, 'w') as file:
        for date in tasks:
            file.write(f"{date}:{';'.join(tasks[date])}\n")


def today_date() -> str:
    return datetime.today().strftime('%d-%m-%Y')


def print_help():
    print("""You can use commands:
help - display available commands
todo - display tasks for today
add_task - add task
delete_task - mark task as done and delete it
exit - to exit""")

def main():
    tasks = read_tasks()
    print_tasks(tasks, today_date())
    print("Type help for available commands")

    while True:
        cmd = input(">>> ")
        if cmd == "help":
            print_help()
        elif cmd == "todo":
            print_tasks(tasks, today_date())
        elif cmd == "add_task":
            strdate = input("Enter the deadline (DD-MM-YYYY):")
            name = input("Enter name of task:")
            priority = 0 if strdate in tasks else 1
            length = len(tasks[strdate]) if strdate in tasks else 1
            while not 1 <= priority <= (length + 1):
                print_tasks(tasks, strdate)
                priority = int(input("Enter priority: "))
                if not 1 <= priority <= (length + 1):
                    print("Invalid priority")
            add_task(tasks, strdate, name, priority - 1)
        elif cmd == "delete_task":
            strdate = input("Enter the deadline (DD-MM-YYYY):")
            name = input("Enter name of task:")
            if strdate in tasks:
                delete_task(tasks, strdate, name)
                print("task deleted successfully")
        elif cmd == "exit":
            break
        else:
            print("Undefined command type 'help' for available commands")

    write_tasks(tasks)


if name == "main":
    main()
