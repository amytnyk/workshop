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