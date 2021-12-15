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


def today_date() -> str:
    return datetime.today().strftime('%d-%m-%Y')


def print_help():
    print("""You can use commands:
help - display available commands
todo - display tasks for today
add_task - add task
delete_task - mark task as done and delete it
exit - to exit""")
