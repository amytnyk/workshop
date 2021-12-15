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